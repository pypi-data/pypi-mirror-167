import pyspark
from pyspark.sql import functions
from pyspark.sql.functions import expr

from tecton_core.query.nodes import ConvertEpochToTimestamp
from tecton_core.query.nodes import CustomFilterNode
from tecton_core.query.nodes import FeatureTimeFilterNode
from tecton_core.query.nodes import RenameColsNode
from tecton_core.query.nodes import RespectFSTNode
from tecton_core.query.nodes import RespectTTLNode
from tecton_core.query.nodes import SetAnchorTimeNode
from tecton_spark import materialization_plan
from tecton_spark.partial_aggregations import TEMPORAL_ANCHOR_COLUMN_NAME
from tecton_spark.query import translate
from tecton_spark.query.node import SparkExecNode
from tecton_spark.time_utils import convert_epoch_to_timestamp_column
from tecton_spark.time_utils import convert_timestamp_to_epoch


class CustomFilterSparkNode(SparkExecNode):
    def __init__(self, node: CustomFilterNode):
        self.input_node = translate.spark_convert(node.input_node)
        self.filter_str = node.filter_str

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        input_df = self.input_node.to_dataframe(spark)
        return input_df.filter(self.filter_str)


class FeatureTimeFilterSparkNode(SparkExecNode):
    def __init__(self, node: FeatureTimeFilterNode):
        self.input_node = translate.spark_convert(node.input_node)
        self.time_filter = node.time_filter
        self.policy = node.policy
        self.timestamp_field = node.timestamp_field

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        input_df = self.input_node.to_dataframe(spark)
        return materialization_plan._apply_or_check_feature_data_time_limits(
            spark, input_df, self.policy, self.timestamp_field, self.time_filter
        )


class TimeFilterSparkNode(SparkExecNode):
    def __init__(self, node: FeatureTimeFilterNode):
        self.input_node = translate.spark_convert(node.input_node)
        self.start_time = node.start_time
        self.end_time = node.end_time
        self.timestamp_field = node.timestamp_field

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        input_df = self.input_node.to_dataframe(spark)
        if self.start_time and self.end_time:
            return input_df.filter(
                (input_df[self.timestamp_field] >= self.start_time) & (input_df[self.timestamp_field] < self.end_time)
            )
        if self.start_time:
            return input_df.filter(input_df[self.timestamp_field] >= self.start_time)
        if self.end_time:
            return input_df.filter(input_df[self.timestamp_field] < self.end_time)


class SetAnchorTimeSparkNode(SparkExecNode):
    def __init__(self, node: SetAnchorTimeNode):
        # Anchor time for retrieval must be offset by data delay
        self.input_node = translate.spark_convert(node.input_node)
        self.offline = node.offline
        self.feature_store_format_version = node.feature_store_format_version
        self.batch_schedule_in_feature_store_specific_version_units = (
            node.batch_schedule_in_feature_store_specific_version_units
        )
        self.timestamp_field = node.timestamp_field
        self.for_retrieval = node.for_retrieval
        self.data_delay_seconds = node.data_delay_seconds

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        input_df = self.input_node.to_dataframe(spark)
        if self.for_retrieval:
            # TODO(brian) Perhaps for retrieval we should also account for difference in data availability for batch vs stream,
            anchor_time_val = convert_timestamp_to_epoch(
                functions.col(self.timestamp_field) - expr(f"interval {self.data_delay_seconds} seconds"),
                self.feature_store_format_version,
            )
            # batch_schedule_in_feature_store_specific_version_units will be 0 for continuous
            if self.batch_schedule_in_feature_store_specific_version_units == 0:
                df = input_df.withColumn(TEMPORAL_ANCHOR_COLUMN_NAME, anchor_time_val)
            else:
                df = input_df.withColumn(
                    TEMPORAL_ANCHOR_COLUMN_NAME,
                    anchor_time_val
                    - anchor_time_val % self.batch_schedule_in_feature_store_specific_version_units
                    - self.batch_schedule_in_feature_store_specific_version_units,
                )
        else:
            anchor_time_val = convert_timestamp_to_epoch(
                functions.col(self.timestamp_field), self.feature_store_format_version
            )
            df = input_df.withColumn(
                TEMPORAL_ANCHOR_COLUMN_NAME,
                anchor_time_val - anchor_time_val % self.batch_schedule_in_feature_store_specific_version_units,
            )
        if not self.offline:
            MATERIALIZED_RAW_DATA_END_TIME = "_materialized_raw_data_end_time"
            df = df.withColumn(
                MATERIALIZED_RAW_DATA_END_TIME,
                functions.col(TEMPORAL_ANCHOR_COLUMN_NAME)
                + self.batch_schedule_in_feature_store_specific_version_units,
            ).drop(TEMPORAL_ANCHOR_COLUMN_NAME)
        return df


class RenameColsSparkNode(SparkExecNode):
    def __init__(self, node: RenameColsNode):
        self.input_node = translate.spark_convert(node.input_node)
        self.mapping = node.mapping

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        input_df = self.input_node.to_dataframe(spark)
        for old_name, new_name in self.mapping.items():
            if new_name:
                input_df = input_df.withColumnRenamed(old_name, new_name)
            else:
                input_df = input_df.drop(old_name)
        return input_df


class ConvertEpochToTimestampSparkNode(SparkExecNode):
    def __init__(self, node: ConvertEpochToTimestamp):
        self.input_node = translate.spark_convert(node.input_node)
        self.feature_store_formats = node.feature_store_formats

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        input_df = self.input_node.to_dataframe(spark)
        for name, feature_store_format_version in self.feature_store_formats.items():
            input_df = input_df.withColumn(
                name,
                convert_epoch_to_timestamp_column(functions.col(name), feature_store_format_version),
            )
        return input_df


class RespectFSTSparkNode(SparkExecNode):
    def __init__(self, node: RespectFSTNode):
        self.input_node = translate.spark_convert(node.input_node)
        self.feature_start_time = node.feature_start_time
        self.retrieval_time_col = node.retrieval_time_col
        self.features = node.features

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        ret = self.input_node.to_dataframe(spark)
        cond = functions.col(self.retrieval_time_col) >= functions.lit(self.feature_start_time)
        # select all non-feature cols, and null out any features outside of feature start time
        project_list = [col for col in ret.columns if col not in self.features]
        for c in self.features:
            newcol = functions.when(cond, functions.col(f"`{c}`")).otherwise(functions.lit(None)).alias(c)
            project_list.append(newcol)
        return ret.select(project_list)


class RespectTTLSparkNode(SparkExecNode):
    def __init__(self, node: RespectTTLNode):
        self.input_node = translate.spark_convert(node.input_node)
        self.ttl = node.ttl
        self.retrieval_time_col = node.retrieval_time_col
        self.source_time_col = node.source_time_col
        self.features = node.features

    def to_dataframe(self, spark: pyspark.sql.SparkSession) -> pyspark.sql.DataFrame:
        ret = self.input_node.to_dataframe(spark)
        cond = functions.unix_timestamp(functions.col(self.retrieval_time_col)) - functions.unix_timestamp(
            functions.col(self.source_time_col)
        ) < functions.lit(self.ttl.in_seconds())
        # select all non-feature cols, and null out any features outside of ttl
        project_list = [col for col in ret.columns if col not in self.features]
        for c in self.features:
            newcol = functions.when(cond, functions.col(c)).otherwise(functions.lit(None)).alias(c)
            project_list.append(newcol)
        return ret.select(project_list)

from enum import Enum, IntEnum, auto


class RuleExecutionStatus(Enum):
    STARTED = 1
    RUNNING = 2
    ERRORED = 3
    WARNING = 4
    SUCCESSFUL = 5
    ABORTED = 6


class FailureStrategy(IntEnum):
    DoNotFail = auto()
    FailOnError = auto()
    FailOnWarning = auto()


class PolicyType(Enum):
    DATA_QUALITY = 'DATA-QUALITY'
    RECONCILIATION = 'RECONCILIATION'


class AssetSourceType(Enum):
    BIGQUERY = 'BIGQUERY'
    REDSHIFT = 'REDSHIFT'
    SNOWFLAKE = 'SNOWFLAKE'
    TERADATA = 'TERADATA'
    HIVE = 'HIVE'
    HBASE = 'HBASE'
    AZURE_MSSQL = 'AZURE_MSSQL'
    AZURE_DATALAKE = 'AZURE_DATALAKE'
    AWS_GLUE = 'AWS_GLUE'
    AWS_S3 = 'AWS_S3'
    HDFS = 'HDFS'
    GCS = 'GCS'
    KAFKA = 'KAFKA'
    MYSQL = 'MYSQL'
    MEMSQL = 'MEMSQL'
    POSTGRESQL = 'POSTGRESQL'
    TABLEAU = 'TABLEAU'
    ORACL = 'ORACLE'
    AWS_ATHENA = 'AWS_ATHENA'
    DATABRICKS = 'DATABRICKS'
    MONGO = 'MONGO'
    MODEL_BAG = 'MODEL_BAG'
    FEATURE_BAG = 'FEATURE_BAG'
    PRESTO = 'PRESTO'
    DB2 = 'DB2'
    CLICKHOUSE = 'CLICKHOUSE'
    VIRTUAL_DATASOURCE = 'VIRTUAL_DATASOURCE'


DATA_QUALITY = 'DATA_QUALITY'
RECONCILIATION = 'RECONCILIATION'

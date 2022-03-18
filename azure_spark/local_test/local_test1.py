import os
from datetime import datetime
from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, col, from_unixtime
from pyspark.sql.functions import year, month, dayofmonth, hour

spark = (SparkSession
        .builder
        .appName("Connect_Azure_Storage")
        .master("local[*]")
        .config("spark.streaming.stopGracefullyOnShutdown", "true")
        .config("spark.sql.streaming.schemaInference", "true")
        .getOrCreate())

spark.conf.set("spark.sql.shuffle.partitions", "5")

df = spark.createDataFrame(
    [
        (1, "Documentai"),  # Add your data here
        (2, "Regulatoryai"),
        (3, "Securityai"),
        (4, "Russia"),
        (5, "Ukraine"),
        (6, "United States of America")
    ],
    "id int, label string",  # add column names and types here
)

df.show()
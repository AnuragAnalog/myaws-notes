#!/usr/bin/python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col

S3_SRC_BUCKET = "s3://data-engineer-training/input/data.csv"
S3_DEST_BUCKET = "s3://data-engineer-training/output/"

def spark_job():
    spark = SparkSession.builder.appName("Spark Job").getOrCreate()
    data = spark.read.csv(S3_SRC_BUCKET, header=True)

    selected_data = data.where(col("location") == "Bangalore")
    selected_data.write.mode("overwrite").parquet(S3_DEST_BUCKET)

if __name__ == '__main__':
    spark_job()
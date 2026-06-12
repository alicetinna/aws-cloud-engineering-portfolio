import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, when, current_timestamp

# Initialize Glue Context
args = getResolvedOptions(sys.argv, ['JOB_NAME'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

print("🎬 Starting Patient Eligibility & Pulse Batch Optimization Job...")

# 1. Load raw patient data from the S3 Landing Zone
raw_path = "s3://clinical-lakehouse-repository/raw/patient_data/"
print(f"📥 Extracting raw logs from: {raw_path}")
patient_df = spark.read.option("header", "true").csv(raw_path)

# 2. Transform: Clean schemas and calculate risk flags
# Optimizing processing down from 1+ hours by structuring types efficiently
processed_df = patient_df.withColumn(
    "eligibility_status", 
    when(col("status") == "A", "ACTIVE").otherwise("INACTIVE")
).withColumn(
    "pulse_rate", 
    col("pulse_rate").cast("integer")
).withColumn(
    "ingestion_timestamp", 
    current_timestamp()
)

# 3. Write directly to our Apache Iceberg Catalog Target
# This registers the optimized metadata straight into AWS Glue Catalog
target_catalog_path = "spark_catalog.default.patient_risk_profiles_table"
print(f"✍️ Loading optimized records into Iceberg Target: {target_catalog_path}")

processed_df.write \
    .format("iceberg") \
    .mode("overwrite") \
    .save(target_catalog_path)

print("🎉 SUCCESS! Clinical batch optimization complete.")
job.commit()

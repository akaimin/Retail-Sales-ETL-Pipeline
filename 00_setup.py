# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
CATALOG = "workspace"
SCHEMA = "retail_sales_dw"
VOLUME = "file_folder"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")

print(f"Schema : {CATALOG}.{SCHEMA}")
print(f"Volume : /Volumes/{CATALOG}/{SCHEMA}/{VOLUME}")
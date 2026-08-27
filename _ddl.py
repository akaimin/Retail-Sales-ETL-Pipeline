# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
CATALOG = "workspace"
SCHEMA = "retail_sales_dw"
VOLUME = "file_folder"
TARGET_DIR = f"/Volumes/{CATALOG}/{SCHEMA}/{VOLUME}"

spark.sql(f"CREATE SCHEMA IF NOT EXISTS {CATALOG}.{SCHEMA}")
spark.sql(f"CREATE VOLUME IF NOT EXISTS {CATALOG}.{SCHEMA}.{VOLUME}")

# COMMAND ----------

# dbutils.widgets.text("source_dir", "", "Source directory")
# source_dir = dbutils.widgets.get("source_dir").strip()
source_dir = "/Workspace/Users/worada.wongtayan@gmail.com/Retail-Sales-ETL-Pipeline/file_to_volume"

# COMMAND ----------

if not source_dir:
    raise ValueError(
        "source_dir is required. Example: /Workspace/Users/<user>/Retail-Sales-ETL-Pipeline/file_to_volume"
    )

files = dbutils.fs.ls(source_dir)
source_files = [
    f.path for f in files
    if (f.name.startswith("shop_name_") and f.name.endswith(".csv"))
    or (f.name.startswith("fact_sales_") and f.name.endswith(".parquet"))
]

if not source_files:
    raise FileNotFoundError(f"No generated source files found in: {source_dir}")

for source_file in source_files:
    file_name = source_file.rsplit("/", 1)[-1]
    target_file = f"{TARGET_DIR}/{file_name}"
    dbutils.fs.cp(source_file, target_file, True)
    print(f"Copied: {file_name}")

print(f"Total source files copied: {len(source_files)}")
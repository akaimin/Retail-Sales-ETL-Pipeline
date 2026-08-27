# Retail Sales DW — workspace.retail_sales_dw

## Unity Catalog
- Catalog: `workspace`
- Schema: `retail_sales_dw`
- Volume: `manual_file_folder`

## Tables
- `workspace.retail_sales_dw.config_table`
- `workspace.retail_sales_dw.shop_name_bronze`
- `workspace.retail_sales_dw.shop_name_silver`
- `workspace.retail_sales_dw.shop_name_bad_record`
- `workspace.retail_sales_dw.fact_sales_bronze`
- `workspace.retail_sales_dw.fact_sales_silver`
- `workspace.retail_sales_dw.fact_sales_bad_record`
- `workspace.retail_sales_dw.gold_daily_sales_kpi`

## Dynamic files
- `shop_name_*.csv`
- `fact_sales_*.parquet`
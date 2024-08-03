import os
import json
import boto3

import pandas as pd

from io import StringIO
from sqlalchemy import create_engine

# AWS credentials and region
aws_access_key = os.environ.get("aws_access_key")
aws_secret_key = os.environ.get("aws_secret_key")
# region_name = '<your-region>'

# S3 bucket and file details
bucket_name = '<bucket-name>'
file_prefix = '<file-name>'

# RDS connection details
database_name = '<db-name>'
table_name = '<table-name>'
rds_host = '<rds-endpoint>'
rds_port = '<rds-instance-port>'
rds_user = '<rds-username>'
rds_password = '<rds-password>'

def lambda_handler(event, context):
    s3_client = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key)

    response = s3_client.get_object(Bucket=bucket_name, Key=file_prefix)
    content = response["Body"]
    df = pd.read_csv(StringIO(response['Body'].read().decode('utf-8')))
    
    # Connect to RDS
    conn_str = f'mysql+pymysql://{rds_user}:{rds_password}@{rds_host}:{rds_port}/{database_name}'
    engine = create_engine(conn_str)

    # Write the DataFrame to RDS
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
    engine.dispose()

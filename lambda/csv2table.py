#!/usr/bin/python3

import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('csv_table')

def lambda_handler(event, context):
    # Get the bucket name and the file name
    bucket = event['Records'][0]['s3']['bucket']['name']
    csv_file = event['Records'][0]['s3']['object']['key']

    # Get the csv file object
    csv_file_obj = s3_client.get_object(Bucket=bucket, Key=csv_file)
    csv_data = csv_file_obj['Body'].read().decode('utf-8')
    csv_records = csv_data.split('\n')

    # Insert each and every row into the table
    for row in csv_records:
        table.put_item(
            Item={
                'id': row.split(',')[0],
                'name': row.split(',')[1],
                'location': row.split(',')[2]
            }
        )

    # Return the success message
    return {
        'statusCode': 200,
        'body': json.dumps('CSV Processed Successfully')
    }

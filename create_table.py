#!/usr/bin/python3

import boto3

def create_table(table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH' # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE' # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N' # Partition key
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S' # Sort key
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5
        }
    )

    return table

if __name__ == '__main__':
    table = create_table('Movies')
    
    # To check the status of the table
    dynamodb = boto3.resource('dynamodb')
    dynamodb.table('Movies')
    print("Table status:", table.table_status)
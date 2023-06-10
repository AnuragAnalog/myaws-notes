#!/usr/bin/python3

import boto3

from boto3.dynamodb.conditions import Key

def create_table(table_name):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.create_table(
        TableName=table_name,
        KeySchema=[
            {
                "AttributeName": "Name",
                "KeyType": "HASH"
            },
            {
                "AttributeName": "Email",
                "KeyType": "RANGE"
            }
        ],
        AttributeDefinitions=[
            {
                "AttributeName": "Name",
                "AttributeType": "S"
            },
            {
                "AttributeName": "Email",
                "AttributeType": "S"
            }
        ],
        ProvisionedThroughput={
            "ReadCapacityUnits": 5,
            "WriteCapacityUnits": 5
        }
    )

    return table

if __name__ == '__main__':
    # table = create_table("Employees")
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table("Employees")

    # Create Operation
    table.put_item(
        Item={
            "Name": "Mark Wilbur",
            "Email": "markwilbur@dataengineer.cloud",
            "Department": "IT"
        }
    )

    # Read Operation
    answer = table.query(
        KeyConditionExpression=Key("Name").eq("Mark Wilbur")
    )
    print(answer["Items"])

    # Update Operation
    table.update_item(
        Key={"Name": "Mark Wilbur", "Email": "markwilbur@dataengineer.cloud"},
        ExpressionAttributeValues={
            ":department": "Finance"
        },
        UpdateExpression="SET Department = :department"
    )

    # Delete Operation
    table.delete_item(
        Key={"Name": "Mark Wilbur", "Email": "markwilbur@dataengineer.cloud"}
    )

    # To check the status of the table
    dynamodb = boto3.resource('dynamodb')
    dynamodb.Table('Employees')
    print("Table status:", table.table_status)
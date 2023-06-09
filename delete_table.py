#!/usr/bin/python3

import boto3

def delete_table(table_name):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    table.delete()
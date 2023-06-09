#!/usr/bin/python3

import json
import boto3
import decimal

def load_data(table_name, data):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    for movie in data:
        year = int(movie['year'])
        title = movie['title']
        info = movie['info']

        print("Adding movie:", year, title)

        table.put_item(
           Item=movie
        )

if __name__ == '__main__':
    # Open the movies json file
    with open("movies.json") as json_file:
        data = json.load(json_file, parse_float = decimal.Decimal)
    
    load_data('Movies', data)
    
    # To check the status of the table
    dynamodb = boto3.resource('dynamodb')
    dynamodb.table('Movies')
    print("Table status:", table.table_status)
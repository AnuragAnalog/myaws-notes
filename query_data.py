#!/usr/bin/python3

import boto3

from boto3.dynamodb.conditions import Key

def query_data(table_name, year, title):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)

    response = table.query(
        KeyConditionExpression=Key('year').eq(year) & Key('title').eq(title)
    )

    return response['Items']

if __name__ == '__main__':
    movies = query_data('Movies', 2015, 'The Big New Movie')
    
    for movie in movies:
        print(movie['year'], ":", movie['title'])
        print(movie['info']['plot'])
        print("Actors:", ", ".join(movie['info']['actors']))
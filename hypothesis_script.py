import requests
import json
import csv

api_url = 'https://api.hypothes.is/api/search'
parameters = {'wildcard_uri': 'https://gdprhub.eu/*', 'limit': '200'}

request = requests.get(api_url, params=parameters)
annotations = json.loads(request.content)
tags_uri = []

for annotation in annotations['rows']:
    for tag in annotation['tags']:
        tags_uri.append([tag, annotation['uri']])

#print(tags_uri)

fields = ['Tag', 'URI']
with open('tags.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(fields)
    write.writerows(tags_uri)
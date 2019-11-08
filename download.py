#!/usr/bin/env python3

import requests
import json
import time
import pathlib

import auth

page = 1

while True:

    url = 'https://memsource.zendesk.com/api/v2/help_center/en-us/articles.json?page={}'.format(page)
    print(f"Requesting {url}")
    headers = {'Content-Type': 'application/json'}
    response = requests.get(url, auth=auth.get_auth(), headers=headers)

    data = json.loads(response.text)

    if len(data['articles']) == 0:
        break

    for article in data["articles"]:
        dirname = 'html/{}/{}'.format(article['section_id'], article['id'])
        pathlib.Path(dirname).mkdir(parents=True, exist_ok=True)
        html_filename = '{}/{}.html'.format(dirname, article['id'])
        json_filename = '{}/{}.json'.format(dirname, article['id'])
        print(f"Writing {html_filename}")
        f = open(html_filename, 'w')
        body = article['body'] if article['body'] else ""
        f.write(body)
        f.close()

        json_article = article.copy()
        del json_article['body']
        f = open(json_filename, 'w')
        f.write(json.dumps(json_article, indent=4, sort_keys=True))
        f.close()
    
    page += 1
    time.sleep(1)


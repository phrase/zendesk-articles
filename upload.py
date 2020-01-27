#!/usr/bin/env python3

import json
import os
import sys
import time

import requests

import auth

article_limit = None
if len(sys.argv) > 1:
    article_limit = sys.argv[1]

rootDir = 'html'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        article, extension = os.path.splitext(fname)
        if extension == '.html':
            if article_limit is None or article_limit == article:
                url = 'https://memsource.zendesk.com/api/v2/help_center/articles/{}/translations/en-us.json'.format(
                    article)
                headers = {'Content-Type': 'application/json'}

                print(f"Requesting GET {url}")
                response = requests.get(url, auth=auth.get_auth(), headers=headers)
                data = json.loads(response.text)

                f = open(f"{dirName}/{fname}", "r")
                body = f.read()

                if "translation" in data:
                    if data["translation"]["body"] == body:
                        print(f"No update to article {article}")
                    else:
                        new_data = {"translation": {"body": body}}
                        print(f"Requesting PUT {url}")
                        response = requests.put(url, auth=auth.get_auth(), headers=headers, data=json.dumps(new_data))
                        print(response)
                else:
                    print(f"Article {article} not found")

                time.sleep(0.1)

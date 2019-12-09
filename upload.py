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
                print(f"Requesting {url}")
                headers = {'Content-Type': 'application/json'}
                f = open(f"{dirName}/{fname}", "r")
                data = {"translation": {"body": f.read()}}
                response = requests.put(url, auth=auth.get_auth(), headers=headers, data=json.dumps(data))
                print(response)
                time.sleep(0.1)

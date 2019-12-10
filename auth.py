#!/usr/bin/env python3

import os

def get_auth():
    return '{}/token'.format(os.getenv('ZENDESK_USER')), os.getenv('ZENDESK_TOKEN')


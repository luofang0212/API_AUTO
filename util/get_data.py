#!/usr/bin/env python
# -*- coding: utf-8 -*-

from util.HttpRequest import HttpRequest

class GetData:
    login_url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
    login_data = {'phone': '17267723687', 'pwd': 'love920212'}
    res_1 = HttpRequest().http_request('post', login_url, login_data)
    USER_TOKEN = res_1.json()['data']['token']
    PHONE=13011110001



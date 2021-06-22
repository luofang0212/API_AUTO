#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 封装http request请求方式
class HttpRequest:

     def http_request(self,method,url,data=None,headers=None,cookies=None,verify=False):
          #get
          if method.lower() == 'get':
               res = requests.get(url, data=data, headers=headers, cookies=cookies)
          #post
          elif method.lower() == 'post':
               res = requests.post(url, data=data,headers=headers, cookies=cookies)
          else:
               print('不支持该方法')
          return res


if __name__ == '__main__':
     # post 登陆
     login_url = 'https://api.xdclass.net/pub/api/v1/web/web_login'
     login_data = {'phone': '17267723687', 'pwd': 'love920212'}
     res_1 = HttpRequest().http_request('post',login_url,login_data)
     print("登录接口响应信息： ",res_1.json())
     user_token = res_1.json()['data']['token']
     print(100*'-')
  # get  用户信息
     user_url = 'https://api.xdclass.net/pub/api/v1/web/user_info'
     user_data = {}
     headers = {
          'token': '{0}'.format(user_token)
     }
     res_2 = HttpRequest().http_request('geT',user_url,user_data,headers=headers)
     print("用户信息接口响应信息： ",res_2.json())

     # post  收藏
     save_url = 'https://api.xdclass.net/user/api/v1/favorite/save'
     save_data = {'video_id':100000010010}
     headers = {
          'token':'{0}'.format(user_token)
     }
     res_3 = HttpRequest().http_request('post', save_url, save_data, headers=headers)
     print("收藏接口响应信息： ", res_3.json())
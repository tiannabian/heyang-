#encoding = utf-8
# __author__ = '何旺彤'

import requests

class HttpRequest:

    def http_request(self, url, param, method, cookies):
        if method.upper() == 'GET':
            try:
                resp = requests.get(url, params=param, cookies=cookies)
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper() == 'POST':
            try:
                resp = requests.post(url, data=param, cookies=cookies)
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('输入有误')
        return resp.json()

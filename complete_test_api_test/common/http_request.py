#encoding = utf-8
# __author__ = '何旺彤'

import requests
# #登陆请求
# url = 'https://account.xiaomi.com/pass/serviceLogin?'
# param = {'mobilephone':'1512997821','pwd':'p@ssw0rd'}
#
# #发送一个get请求
# resp = requests.get(url, params=param)
# #print(resp.text)
# print(resp.json)
#
# #发送一个post请求
# resp = requests.post(url, data = param)
# #print(resp.text)
# print(resp.json)
class HttpRequest:

    def http_request(self,url,param,method,cookies):
        if method.upper()=='GET':
            try:
                resp=requests.get(url,params=param,cookies=cookies)
            except Exception as e:
                print('get请求出错了：{}'.format(e))
        elif method.upper()=='POST':
            try:
                resp=requests.post(url,data=param,cookies=cookies)
            except Exception as e:
                print('post请求出错了：{}'.format(e))
        else:
            print('输入有误')
        return resp.json()

#测试代码
if __name__ == '__main__':
    pass
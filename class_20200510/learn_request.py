#coding: utf-8
#author = hewangtong
#date = 2020/5/10

import requests

url = 'http://47.107.168.87:8080/futureloan/mvc/api/member/register'
param = {'mobilephone':'18813989009', 'pwd':'123456', 'regname':'lemonhuahua'}
resp = requests.get(url, params=param)
print(resp)
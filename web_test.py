__author__ = '何旺彤'
import requests
res = requests.get('https://github.com/')
print(res)
from selenium import  webdriver
driver = webdriver.Firefox()
driver.get('https://github.com/')
print("我爱南志姣")


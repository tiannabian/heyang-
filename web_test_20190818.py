__author__ = '何旺彤'


#########################################文件传输


import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import  Keys

driver = Chrome()
driver.implicitly_wait(20)

#函数注解
def wait_find_element(loactor) -> WebElement:
    wait = WebDriverWait(driver, timeout=30, poll_frequency=0.5)
    input_ele = wait.until(ec.presence_of_all_elements_located(loactor))
    return input_ele

driver.get('file:///D:/Users/%E4%BD%95%E6%97%BA%E5%BD%A4/PycharmProjects/heyang-/index.html')

#定位文件发送的元素
#   1、如果是input可以直接输入路径的，那么直接调send_keys输入路径
e = driver.find_element_by_name('myfile')
e.submit()

#    2、非input标签的上传，则需要借助第三方工具
      #2.1 Autolt 我们去调用其生成的au3或exe文件
      #2.2 SendKeys 第三方库（目前只支持到2.7版本） 网址：https:pypi.python.org/pypl/SendKeys
      #2.3 Python pywin32库，识别对话框句柄，进而操作  工具winspy64

import win32gui
import win32con

#找到对应的窗口
dialog = win32gui.FindWindow("#32770", "打开")#一级窗口(上传窗口),32770为句柄
#找到窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级（子窗口）
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)#三级
edit = win32gui.FindWindowEx(comboBox,0,"Edit",None) #四级
button = win32gui.FindWindowEx(dialog,0,'Button',None)  #二级

#操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,'D;\\apk.txt') #发送文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)#点击打开按钮





########################################################窗口拖动，滚动  原因：特定的时候只有将窗口滚动到某个特定的位置，某个元素才会出现
#第一种方法：发送拖动的js脚本
js_code = "window.scrollTo(0,document.body.scrollHeight)"
driver.execute_script(js_code)


#第二种方法：使用selenium
e.location_once_scrolled_into_view()




###########################################################富文本域
#富文本域 textarea,不能使用send_keys,  需要使用js形式，修改里面的innerHTML

'''
一、web自动化selenium
1、selenium原理：通过http协议搭建的webdriver接口，一方面，它通过一个servers服务，使用python里面的subprocess库自动的运行了chromedriver.exe文件
并在对应的窗口开一个webdriver服务；另一方面，chromeRemoteConnection==>类似于requests urlib3 ==> requsts.post(host:9515/接口地址)
问题：使用requests库访问对应的webdriver接口实现以下功能：
1、访问百度页面2、通过id形式查找搜索输入框元素并打印返回结果3、通过css selector查找搜索输入框元素并打印返回结果
import requests
from selenium import webdriver
driver = webdriver.Chrome()
#访问百度页面
sessionid = driver.session_id  #webdriver的接口地址，requests,接口地址，commands = []
url = 'http://localhost:9515/session/{}/url'.format(sessionid)
baidu_url = 'http://www.baidu.com'
data = {'url':baidu_url}
requests.post(url,json=data)

#获取页面元素，接口文档没有，不知道参数要传递什么
url = 'http://localhost:9515/session/{}/element'.format(sessionid)
data = {'using':"css selector",'value':"#kw"}
res = requests.post(url, json=data)
print(res)


'''








__author__ = '何旺彤'


#########################################文件传输  面试题


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
dialog = win32gui.FindWindow("#32770", "打开")#一级窗口
#找到窗口
ComboBoxEx32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)  #二级
comboBox = win32gui.FindWindowEx(ComboBoxEx32,0,"ComboBox",None)#三级
edit = win32gui.FindWindowEx(comboBox,0,"Edit",None) #四级
button = win32gui.FindWindowEx(dialog,0,'Button',None)  #四级

#操作
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,'D;\\apk.txt') #发送文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)













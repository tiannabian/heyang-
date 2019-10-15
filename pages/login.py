__author__ = '何旺彤'
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome

class LoginPage:
    """登录页面，PageObject"""
    def __init__(self, driver):
        self.driver = driver
        self.url = "http://120.78.128.25:8765/Index/login.html"

    def login(self, username, pwd):
        """登陆函数封装"""

        #2、访问登录页面visit_login_page
        self.driver.get(self.url)

        #3、定位元素find_element
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.NAME, 'phone')))  #可利用括号以及括号里面的逗号进行换行
        pwd_ele = WebDriverWait(self.driver, 20).until(ec.presence_of_element_located((By.XPATH, "//input[@name='password']")))

        #4、发送用户名密码，提交submit
        user_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        user_ele.submit()
        return self.driver

    def get_flash_info(self):
        """获取错误信息"""
        flash_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, 'form-error-info')))
        return flash_ele

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
        user_ele = self.get_user_info()
        pwd_ele = self.get_pwd_info()

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

    def clear_user_info(self):
        """清空用户数据"""
        #清空用户名clear_username()
        self.clear_username()
        #清空密码clear_pwd()
        self.clear_pwd()

    def clear_username(self):
        """清空用户名"""
        #定位用户 get_username()
        return self.get_user_info().clear()

    def clear_pwd(self):
        """清空密码"""
        return self.get_pwd_info().clear()

    def get_user_info(self):
        """定位用户名"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.NAME, 'phone')))
        return user_ele

    def get_pwd_info(self):
        """定位密码输入"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//input[@name='password']")))
        return user_ele
######为什么要封装这么多函数？1、当项目越来越大的时候，只需要使用这些函数，不需要复制具体的代码了；2、增加代码的可读性；3、中级要求，10来行，函数的颗粒度













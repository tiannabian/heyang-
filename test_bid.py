__author__ = '何旺彤'

"""测试投资功能
前置条件：
1、登陆
2、有没有余额 查询余额，如果没有余额，需要充值，可以使用接口充值、修改数据库充值，或者直接充值100亿
3、标有没有钱
"""

import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
from pages.login import LoginPage
from selenium.webdriver.remote import webdriver
from test_data.login import user_info_success


class TestLogin(unittest.TestCase):

    def setUp(self)-> None:
        """登陆"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_info_success["username"], user_info_success["pwd"])

    def tearDown(self)-> None:   #箭头符号表示函数注解表示返回的是None
        self.driver.quit()

    def test_bid_success(self):
        #在首页选择标的 choice_bid() ,点击投标

        #
        pass





#1、选择一个标点击投标  2、输入投资金额，点击投标
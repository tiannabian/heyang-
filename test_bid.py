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
from pages.index import IndexPage
from pages.bid import BidPage
from test_data.bid import invest_money
from pages.user import UserPage


class TestBid(unittest.TestCase):

    def setUp(self)-> None:
        """登陆"""
        self.driver = webdriver.Chrome()
        self.login_page = LoginPage(self.driver)
        self.login_page.login(user_info_success["username"], user_info_success["pwd"])
        self.bid_page = BidPage(self.driver)

    def tearDown(self)-> None:   #箭头符号表示函数注解表示返回的是None
        self.driver.quit()

    def test_bid_success(self):
        #在首页选择标的 choice_bid() ,点击投标
        IndexPage(self.driver).choice_bid()

        #定位投资输入框元素
        e = self.bid_page.get_bid_input_element()

        expect = e.get_attribute('data-amount')
        print(expect)

        #发送投资金额
        e.send_keys(invest_money)
        #点击投标
        self.bid_page.click_bid_submit()
        #获取可用余额
        actual_money_str = UserPage(self.driver).get_user_money()
        actual_money = float(actual_money_str)
        #断言相关操作
        self.assertTrue(int(expect*100)-invest_money == int(actual_money))



if __name__ == '__main__':
    unittest.main()







#1、选择一个标点击投标  2、输入投资金额，点击投标
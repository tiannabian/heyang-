__author__ = '123456'
# coding=utf-8
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
from pages.base import BasePage


class UserPage(BasePage):
    """用户页面"""
    user_money_locator = (By.CSS_SELECTOR, '.color_sub')

    def get_user_money(self):
        """获取可用余额"""
        e = self.wait_presence_element(self.user_money_locator)
        money = e.text[:-1].strip()
        return money  #字符串
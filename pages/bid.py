__author__ = '何旺彤'
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
from pages.base import BasePage

class BidPage(BasePage):
    """投资页面，PageObject"""

    bid_input_locator = (By.XPATH, '//input[contains(@class,"form-control invest-unit-investinput")]')

    def get_bid_input_element(self):
        """获取投标输入框元素"""
        get_bid_input_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((self.bid_input_locator)))
        return get_bid_input_ele







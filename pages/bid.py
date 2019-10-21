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

    bid_submit_locator = (By.XPATH, '//button[contains(@class,"btn btn-special height_style")]')
    #投资激活定位
    alert_active_locator = (By.XPATH, '//div[@class="layui-layer-content"]//button[contains(text(),"查看并激活")]')


    def get_bid_input_element(self):
        """获取投标输入框元素"""
        return self.wait_present_elemrnt(self.bid_input_locator, timeout=20)

    def click_bid_submit(self):
        """点击投标按钮"""
        e = self.wait_clickable_element(self.bid_submit_locator)
        e.click()

    def click_alert(self):
        """点击激活并查看"""
        e = self.wait_clickable_element(self.alert_active_locator)
        e.click()



















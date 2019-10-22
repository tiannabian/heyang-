__author__ = '123456'
# coding=utf-8
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
import logging

class BasePage:
    """投资页面，PageObject"""

    def __init__(self, driver: Chrome):
        self.driver = driver

        pass
    def wait_present_element(self, locator, timeout=10, poll_frequency=0.1):
        """等待元素出现,  定义复杂，调用简单"""
        try:
            user_ele = WebDriverWait(self.driver, timeout, poll_frequency).until(
                ec.presence_of_element_located(locator))
            return user_ele
        except Exception as e:
            #logger
            logging.error("元素定位失败")
            #截屏
            self.driver.save_screenshot('test.jpg')

    def wait_clickable_element(self, locator):
        """等待元素点击"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(locator))
        return user_ele

    def switch(self, name="", if_window=True):
        """窗口切换、iframe、alert"""
        if name == "":
            #切换到默认页面，主页面
            pass

    def click(self):
        pass

    def send_keys(self):
        pass



#(By.XPATH, "//a[@href='/Member/index.html']")
#(By.XPATH, "//a[@href='/Member/index.html']")
#pytest
__author__ = '123456'
# coding=utf-8
import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome

class BasePage:
    """投资页面，PageObject"""

    def __init__(self, driver):
        self.driver = driver

        pass
    def wait_present_element(self, locator):
        """等待元素出现"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(locator))
        return user_ele

    def wait_clickable_element(self, locator):
        """等待元素点击"""
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.element_to_be_clickable(locator))
        return user_ele



#(By.XPATH, "//a[@href='/Member/index.html']")
#(By.XPATH, "//a[@href='/Member/index.html']")
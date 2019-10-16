from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage
__author__ = '123456'
# coding=utf-8

class IndexPage(BasePage):
    """首页类"""

    def __init__(self, driver):
        self.driver = driver

    def get_user_info(self):
        """获取首页的用户信息"""
        #BasePage.wait_present_element()
        user_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']")))
        return user_ele

    def choice_bid(self):
        """选择标的"""
        #定位投标这个按钮

        #点击
        pass
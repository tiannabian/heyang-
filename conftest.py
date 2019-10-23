__author__ = '123456'
# coding=utf-8
import pytest
from selenium.webdriver import Chrom
from pages.login import LoginPage

@pytest.fixture()
def init_web():
    """"""
    driver = Chrom()
    login_page = LoginPage(driver)
    yield driver, login_page #
    driver.quit()

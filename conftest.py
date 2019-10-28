__author__ = '123456'
# coding=utf-8
import pytest
from selenium.webdriver import Chrome
from pages.login import LoginPage

@pytest.fixture()
def init_web():
    """"""
    driver = Chrome()
    login_page = LoginPage(driver)
    yield driver, login_page #
    driver.quit()

@pytest.fixture(scope='class')
def class_web():
    print("class before")
    yield
    print("class after")

@pytest.fixture(scope="moudule", autouse=True) #autouse表示自动运行代码,慎重使用
def moudule_web():
    print("moudule before")
    yield
    print("moudule after")

@pytest.fixture(scope="session")
def session_web():
    print("session before")
    yield
    print("session after")

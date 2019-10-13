__author__ = '何旺彤'
"""测试登录功能"""

import unittest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome
from pages.login import LoginPage

class TestLogin(unittest.TestCase):

    def setUp(self)-> None:
        #浏览器初始化
        self.driver = Chrome()
        #初始化登陆界面
        self.login_page = LoginPage(self.driver)

    def tearDown(self)-> None:   #箭头符号表示函数注解表示返回的是None
        self.driver.quit()

    def test_login_success(self):
        #登陆
        driver = self.login_page.login("18684720553", "python")
        #5、断言,首页的元素
        #user_ele = driver.find_element_by_xpath("//a[@href='/Member/index.html']")#记住这个要进行等待，不等待运行不成功
        user_ele = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']")))
        self.assertTrue("小蜜蜂96027921" in user_ele.text)
        time.sleep(2)
        driver.quit()

        #5、断言,首页的元素
        #user_ele = driver.find_element_by_xpath("//a[@href='/Member/index.html']")#记住这个要进行等待，不等待运行不成功
        user_ele = WebDriverWait(driver, 20).until(
            ec.presence_of_element_located((By.XPATH, "//a[@href='/Member/index.html']")))
        self.assertTrue("小蜜蜂96027921" in user_ele.text)
        time.sleep(2)
        driver.quit()

    #手机号码为空：请输入手机号码
    #手机号码格式不正确：请输入正确的手机号码
    #密码为空：请输入密码
    #密码不正确：弹层：此账号没有经过授权，请联系管理员!
    def test_login_error_one(self):

        driver = self.login_page.login("","")
        #断言
        self.assertTrue(e.text, '请输入手机号码')

    def test_login_error_two(self):
        driver = self.login_page.login(18684720553, "")










if __name__ == '__main__':
    unittest.main()
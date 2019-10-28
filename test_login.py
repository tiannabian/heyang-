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
from pages.index import IndexPage
import ddt
from test_data.login import user_info_error
import pytest
#import init_web



# def init_web():
#     """初始化浏览器"""
#     driver = Chrome()
#     login_page = LoginPage(driver)
#     return driver, login_page
#
#
# def finish_web():
#     """退出浏览器"""
#     init_web().quit()


#@ddt.ddt
@pytest.mark.login
@pytest.mark.c
@pytest.mark.test
#@pytest.mark.usefixture('init_web')#如果要在类的前面调用fixture可以传参数进去
class TestLogin():


    # @classmethod  #类方法
    # def setUpClass(cls) - > None:  #两种方法表示每一个类只执行一次
    #     #浏览器初始化
    #     cls.driver = Chrome()
    #     #初始化登陆界面
    #     cls.login_page = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls) -> None:
    #     cls.driver.quit()
    #
    #
    # def setUp(self)-> None:
    #     pass
    #
    # def tearDown(self)-> None:   #箭头符号表示函数注解表示返回的是None
    #     pass#清空用户信息 clear_user_info()


    #@pytest.mark.login
    def test_login_2_success(self):
        #登陆 login
        # self.driver = Chrome()
        # self.login_page = LoginPage(self.driver)
        self.driver, self.login_page = init_web()
        self.login_page.login("18684720553", "python")
        #5、断言,首页的元素
        #先获取用户信息  get_user_info
        user_ele = IndexPage(self.driver).get_user_info()
        #self.assertTrue("小蜜蜂96027921" in user_ele.text)
        assert("小蜜蜂96027921" in user_ele.text)
        time.sleep(2)
        self.driver.quit()


    #手机号码为空：请输入手机号码
    #手机号码格式不正确：请输入正确的手机号码
    #密码为空：请输入密码
    #密码不正确：弹层：此账号没有经过授权，请联系管理员!
    #####数据不同采用ddt进行数据分离


    #@pytest.mark.login
    #@pytest.mark.skip(reason="这不重要")#mark表示标记
    @ddt.data(*user_info_error)
    @pytest.mark.parametrize('data', user_info_error)
    def test_login_1_error(self, data, session_fixture, init_web):
        """手机号码为空，请输入手机号"""
        #登陆
        #init_web[0]  init_web[1]
        self.driver, self.login_page = init_web()
        self.login_page.login(data['username'], data['pwd'])
        #定位出错信息的元素 get_flash_info()
        flash_ele = self.login_page().get_flash_info()
        #断言
        self.assertTrue(data['expected'] == flash_ele.text)

        self.driver.quit()

        #assert (True)

    def test_login_2_unauth(self, data):
        pass





if __name__ == '__main__':
    unittest.main()

    #随机测试
    #测试用例发现 自动发现
    #测试环境管理  fixture
    #测试报告得生成  pip install pytest-allure
    #重运行机制
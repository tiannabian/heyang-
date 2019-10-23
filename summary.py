__author__ = '123456'
# coding=utf-8

"""
import pytest

@pytest.mark.error
    pass#表示标签
1、为什么要使用pytest?
pytest -m 标签,冒烟测试；
可以放到方法上面也可以放到类上面；
一个方法和类上面可以有多个标签
注意1：mark表达式一定要用双引号
注意2：



缓存文件： .pyc .pyd  .pyo
缓存文件夹：   cache

2、跳过函数
3、可以自动发现测试用例(怎么知道的呢？——符合命名规则test_*.py或者 *_test.py 的文件；以test_开头的函数名； 以Test开头的测试类（没有__init__函数）当中，以test_开头的函数)
4、断言很方便assert
5、非常非常多的插件  重运行  allure测试报告
    pytest -m "demon" --resultlog=report\test.log
    pytest -m demo --junitxml=report\test.xml
    装插件 pip install pytest-html   pytest -m demo --html=report\test.html
6、兼容unittest

7、fixture环境管理非常灵活
yield和return类似，但是函数遇到return停止，遇到yield不停止
作用域 函数、类、模块、会话


pytest的参数化  @pytest.mark.parametrize('data', user_info_error)
不能和unittest同时使用






"""

#coding: utf-8
#author = hewangtong
#date = 2020/5/4

import unittest
import HTMLTestRunnerNew
from class_20200504.learn_unittest import *
from class_20200504 import learn_unittest

#添加用例
suite = unittest.TestSuite()
# suite.addTest(TestAdd('test_001'))  #测试用例的实例
# suite.addTest(TestAdd('test_002'))  #测试用例的实例
# suite.addTest(TestAdd('test_003'))  #测试用例的实例
# suite.addTest(TestAdd('test_004'))  #测试用例的实例

#LOADER专门用来加载测试用例 有两种方式   ddt装饰的用例只能用loader方式
load = unittest.TestLoader()
suite.addTest(load.loadTestsFromTestCase(TestAdd))
#suite.addTest(load.loadTestsFromTestCase(TestSub))

##########方法3  通过测试模块来进行添加
# suite.addTest(load.loadTestsFromModule(learn_unittest))

#执行用例
with open('test.txt', 'w', encoding='utf-8') as file:
    runner = unittest.TextTestRunner(stream=file, descriptions=True, verbosity=2)
    runner.run(suite)

# with open('test_0504.html', 'wb') as file:
#     runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
#                                             verbosity=2,
#                                             title='这是一份测试报告',
#                                             description='这真的是一份测试报告',
#                                             tester='蒲公瑛姑娘')
#     runner.run(suite)

#. 表示一条用例测试通过
#E 表示一条用例报错
#F 表示一条用例测试未通过
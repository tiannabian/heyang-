#coding: utf-8
#author = hewangtong
#date = 2020/5/3
import unittest
from ddt import ddt,data, unpack

test_data_1 = [[1,2,3],[3,-1,2]]
@ddt
#开始对加法进行单元测试了
class TestAdd(unittest.TestCase):
    '''加法测试类'''
    def setUp(self):
        print('-------我们开始测试啦------')

    def tearDown(self):
        print('-------测试结束啦---------')

    @data(*test_data_1)
    @unpack
    def test_001(self,a, b, expected):  #写测试用例，必须以test_开头
        '''测试两个整数相加'''
        c = a+b
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('两个整数相加报错是:{}'.format(e))
            raise e

    # def test_002(self):  #写测试用例，必须以test_开头
    #     '''测试两个负数相加'''
    #     a = -1
    #     b = -2
    #     c = a+b
    #     expected = -3
    #     try:
    #         self.assertEqual(expected, c)
    #     except AssertionError as e:
    #         print('两个负数相加报错是:{}'.format(e))
    #         raise e
    #
    # def test_003(self):  #写测试用例，必须以test_开头
    #     '''测试一正一负相加'''
    #     a = 1
    #     b = -2
    #     c = a+b
    #     expected = -1
    #     try:
    #         self.assertEqual(expected, c)
    #     except AssertionError as e:
    #         print('一正一负相加报错是:{}'.format(e))
    #         raise e
    #     print('这是一个正数和一个负数相加')
    # def test_004(self):  #写测试用例，必须以test_开头
    #     '''测试两个0相加'''
    #     a = 0
    #     b = 0
    #     c = a+b
    #     expected = 0
    #     try:
    #         self.assertEqual(expected, c)
    #     except AssertionError as e:
    #         print('两个0相加报错是:{}'.format(e))
    #         raise e

#开始对减法进行单元测试了
class TestSub(unittest.TestCase):

    def test_005(self):  #写测试用例，必须以test_开头
        '''测试两个0相减'''
        a = 0
        b = 0
        c = a-b
        expected = 0
        try:
            self.assertEqual(expected, c)
        except AssertionError as e:
            print('两个0相减报错是:{}'.format(e))
            raise e
        print('这是两个0相减')

#用例执行的顺序是按照ASCII编码进行的
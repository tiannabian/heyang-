    #coding: utf-8
#author = hewangtong
#date = 2020/5/4
#ddt  data driver test  数据驱动测试
#安装 pip install ddt
from ddt import ddt,data,unpack
import unittest

test_data_1 = [[1,2,3],[3,-1,2]]
test_data_2 = [{'a':1,'b':2,'expected':3},{'a':3,'b':-1,'expected':2}]

@ddt #用来装饰测试类
class TestPringMsg(unittest.TestCase):

    # #data这个函数的参数，是*values,是动态参数  到函数内不会存到一个元组里面，再对元组进行遍历，取到元组的值之后传递给被装饰的函数的参数名
    # @data([1,2,3], (4,5,9))
    # @unpack   #对data传递过来的元组子元素进行拆分，要求是可迭代的，要被装饰的函数进行接受
    # def test_001(self,a, b, expected):
    #     c = a+b
    #     AssertionError(c , expected)
    #     #print('这是执行第:{}条测试用例'.format(a))

    @data(*test_data_2)
    @unpack
    def test_002(self,a, b, expected): #使用字典进行解包的时候，参数需要使用key名称
        c = a+b
        self.assertEqual(c, expected)








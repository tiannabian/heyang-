__author__ = '何旺彤'
import unittest
from ddt import ddt,data
from complete_test.common.http_request import HttpRequest
from complete_test.common.do_excel import DoExcel
from complete_test.common import project_path
from complete_test.common.my_log import MyLog

#测试注册
test_data=DoExcel(project_path.case_path,'register').read_data('RegisterCASE')#获取测试数据
my_log=MyLog()

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t=DoExcel(project_path.case_path,'register')#写入测试结果对象

    def tearDown(self):
        pass

    @data(*test_data)
    def test_cases(self,case):
        global TestResult#全局变量
        method=case['method']
        url=case['URL']
        param=eval(case['Params'])

        #发起测试
        my_log.info('-----正在测试{}模块中的第{}条用例：{}'.format(case['module']))
        my_log.info('-----测试数据是{}'.format())
        resp=HttpRequest().http_request(method,url,param)
        if resp.cookies:#判断请求的cookies是否为空，不为空其实就是true
            setattr(GetData,'COOKIES',resp.cookies)#我们可以更新COOKIES这个全局变量的值
        try:
            self.assertEqual(eval(case['ExceptedResult']),resp.json())
            TestResult='Pass'#请注意这里
        except AssertionError as e:
            TestResult='Fail'
            my_log.error('请求出错了，错误是{}'.format(e))
            raise e#抛出异常
        finally:
            #需要写回实际结果
            self.t.write_back(case['Caseid']+1,8,resp.text)#请注意这里
            self.t.write_back(case['Caseid']+1,9,resp.TestResult)

        my_log.info('实际结果：{}'.format(resp.json))

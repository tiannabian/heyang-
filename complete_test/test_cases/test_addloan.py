__author__ = '何旺彤'
import unittest
from ddt import ddt,data
from complete_test.common.http_request import HttpRequest
from complete_test.common.do_excel import DoExcel
from complete_test.common import project_path
from complete_test.common.my_log import MyLog
from complete_test.common.learn_mysql import DoMysql
from complete_test.common.get_data import GetData
from complete_test.common import get_data
#测试注册
test_data=DoExcel(project_path.case_path,'Addloan').read_data('AddloanCASE')#获取测试数据
my_log=MyLog()

@ddt
class TestCases(unittest.TestCase):

    def setUp(self):
        self.t=DoExcel(project_path.case_path,'Addloan')#写入测试结果对象

    def tearDown(self):
        pass

    @data(*test_data)
    def test_cases(self,case):
        global TestResult#全局变量
        method=case['method']
        url=case['URL']
        param=eval(case['Params'])

        '''
        #替换loan_id
        if case['param'].find('loanid')!=-1:
            param=eval(case['param'].replace('loanid',str(getattr(GetData,'LOAN_ID'))))#因为拿到的是字符串类型
        else:
            param=eval(case['param'])#请求参数
        '''
        params = eval(get_data.replace(case['Param']))


        #发起测试
        my_log.info('-----正在测试{}模块中的第{}条用例：{}'.format(case['module']))
        my_log.info('-----测试数据是{}'.format())
        resp=HttpRequest().http_request(method,url,param,cookies=getattr(GetData,'COOKIES'))

        #判断是否要查询数据库
        if case['sql']!=None:#如果sql语句不为None,进行数据库的查询操作
            loan_id=DoMysql().do_mysql(eval(case['sql'])['sql'],1)#返回的是元祖，所以我们在存储数据的时候，最好是根据索引拿到值之后再去做进一步操作
            setattr(GetData,'LOAN_ID',str(loan_id[0]))#利用反射

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
            self.t.write_back(case['Caseid']+1,9,resp.text)#请注意这里
            self.t.write_back(case['Caseid']+1,10,resp.TestResult)

        my_log.info('实际结果：{}'.format(resp.json))

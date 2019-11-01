__author__ = '何旺彤'

import unittest
import HTMLTestRunnerNew
from complete_test_api_test.test_cases import test_recharge
from complete_test_api_test.test_cases import test_register
from complete_test_api_test.common import project_path

#新建一个测试集
suite=unittest.TestSuite()

#添加用例
loader=unittest.TestLoader
suite.addTest(loader.loadTestsFromTestCase(test_recharge))
suite.addTest(loader.loadTestsFromTestCase(test_register))

#执行测试用例，生成测试报告
with open(project_path.report_path,'wb') as file:
    runner=HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                            verbosity=2,
                                            title='123',
                                            decription='1234',
                                            tester='haha')

    runner.run(suite)#执行用例，传入suite  suite里面是我们收集的测试用例


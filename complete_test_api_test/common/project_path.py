__author__ = '何旺彤'
import os
#文件的路径放这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
#测试用例路径
case_path=os.path.join(project_path,'test_cases','test_api.xlsx')

#测试报告路径
report_path=os.path.join(project_path,'test_result','test_report','test_report.html')

#日志路径
log_path=os.path.join(project_path,'test_result','test_log','test.log')

#配置文件的路径
conf_path=os.path.join(project_path,'conf','case.conf')
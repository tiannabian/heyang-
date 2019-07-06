__author__ = '何旺彤'

from complete_test_api_test import read_config
from complete_test_api_test.common import project_path
import re

config = read_config.ReadConfig(project_path.conf_path)

class GetData:
    '''可以用来动态的更改删除、获取数据'''
    COOKIES=None
    LOAN_ID=None#新添加的标id初始值
    normal_user = config.get_str('data','normal_user' )
    normal_pwd = config.get_str('data','normal_pwd' )
    normal_member_id = config.get_str('data','normal_member_id' )

def replace(target):
    p2 = '#(.*?)#'    #()代表正则表达式里面组的概念
    while re.search(p2, target):
        m = re.search(p2, target)#在目标字符串里面根据正则表达式查找，有目标有匹配的字符串就返回对象
        key = m.group(1)#传参只返回匹配的字符串，也就是当前组的匹配字符
        value = getattr(GetData, key)#拿到我们需要替换的值
        target = re.sub(p2,value,target,count=1)
    return target


#类属型
print(GetData.COOKIES)
print(GetData().COOKIES)
#类的反射可以动态的查看、增加、删除、更改类里面的属性
#利用反射的方法来拿值
print(getattr(GetData,'COOKIES'))#第一个参数是类名  第二个参数是属性的参数名
print(hasattr(GetData,'COOKIES'))#第一个参数是类名  第二个参数是属性的参数名
print(setattr(GetData,'COOKIES','123456'))#第一个参数是类名  第二个参数是属性的参数名  第三个是你要设置的新值

print(delattr(GetData,'COOKIES'))#删除类的某个属性，第一个参数是类名  第二个参数是属性的参数名,
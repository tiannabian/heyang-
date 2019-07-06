__author__ = '何旺彤'
"""
1、什么是正则表达式：
编写一些规范查找需要的字符串
2、组成：原义字符和元字符
3、如何python来解析？
4、使用正则表达式的场景
    参数化
    查找一些特殊的字符：邮箱、手机号码、身份证号码
"""
import re
from complete_test_api_test.common.get_data import GetData
target = "{'mobilephone':'#normal_user#','pwd':'#normal_pwd#'}"
#p = 'normal_user'#原义字符查找
p2 = '#(.*?)#'    #()代表正则表达式里面组的概念

'''
m = re.search(p2, target)#在目标字符串里面根据正则表达式查找，有目标有匹配的字符串就返回对象
print(m)
print(m.group())#不传参的时候返回表达式和匹配的字符串一起
print(m.group(1))#传参只返回匹配的字符串，也就是当前组的匹配字符
mm = re.findall(p2,target)#找到所有匹配的字符，返回的是一个列表
print(mm)
target2 = re.sub(p2,'188109039771',target,count=1)
print(target2)
'''

while re.search(p2, target):
    m = re.search(p2, target)#在目标字符串里面根据正则表达式查找，有目标有匹配的字符串就返回对象
    key = m.group(1)#传参只返回匹配的字符串，也就是当前组的匹配字符
    value = getattr(GetData, key)#拿到我们需要替换的值
    target = re.sub(p2,value,target,count=1)



#coding: utf-8
#author = hewangtong
#date = 2020/5/2

#方法一：
#res = cf.get('name','name_01')
#方法二：
# print(type(eval(cf['name']['name_02'])))
# print(type(eval(cf['name']['name_03'])))
# print(type(eval(cf['name']['name_04'])))
# print(type(eval(cf['name']['name_05'])))
# print(type(eval(cf['name']['name_06'])))

#读取所有的value值都是字符串，如果我们想要原来的数据格式，我们可以使用eval()函数


#写一个配置类
from configparser import ConfigParser

cf = ConfigParser()
cf.read('lemon.conf', encoding='utf-8')
class ReadConfig:
    '''这是一个配置类'''

    def get_int(self, section, option):
        '''从配置文件中获取一个整数'''
        value = cf.getint(section, option)
        return value

    def get_float(self, section, option):
        '''从配置文件中获取一个浮点数'''
        value = cf.getfloat(section, option)
        return value

    def get_boolean(self, section, option):
        '''从配置文件中获取一个布尔值'''
        value = cf.getboolean(section, option)
        return value

    def get_data(self, section, option):
        '''从配置文件中获取一个其他类型数据'''
        value = cf.get(section, option)
        return eval(value)

    def get_str(self, section, option):
        '''从配置文件中获取一个字符串'''
        value = cf.get(section, option)
        return value

if __name__ == '__main__':
    res = ReadConfig().get_data('name','name_03')
    print(res)











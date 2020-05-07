#coding: utf-8
#author = hewangtong
#date = 2020/5/2
from configparser import ConfigParser

class ReadConfig:
    '''这是一个配置类'''
    def __init__(self, file_name):
        self.cf = ConfigParser()
        self.cf.read(file_name, encoding='utf-8')

    def get_int(self, section, option):
        '''从配置文件中获取一个整数'''
        value = self.cf.getint(section, option)
        return value

    def get_float(self, section, option):
        '''从配置文件中获取一个浮点数'''
        value = self.cf.getfloat(section, option)
        return value

    def get_boolean(self, section, option):
        '''从配置文件中获取一个布尔值'''
        value = self.cf.getboolean(section, option)
        return value

    def get_data(self, section, option):
        '''从配置文件中获取一个其他类型数据'''
        value = self.cf.get(section, option)
        return eval(value)

    def get_str(self, section, option):
        '''从配置文件中获取一个字符串'''
        value = self.cf.get(section, option)
        return value

# if __name__ == '__main__':
#     res = ReadConfig('lemon.conf').get_str('name','name_01')
#     print(res)











__author__ = '何旺彤'
from configparser import ConfigParser

class ReadConfig:
    def __init__(self, file_name):
        self.cf = ConfigParser()
        try:
            self.cf.read(file_name, encoding='utf-8')
        except Exception as e:
            print('文件打开报错：{}'.format(e))

    def get_int(self, section, option):
        '''从配置文件里面获取一个整型数据'''
        try:
            value = self.cf.getint(section, option)
            return value
        except Exception as e:
            print('取值报错：{}'.format(e))

    def get_float(self, section, option):
        '''从配置文件中获取一个浮点数'''
        try:
            value = self.cf.getfloat(section, option)
            return value
        except Exception as e:
            print('取值报错：{}'.format(e))

    def get_bool(self, section, option):
        '''从配置文件中获取一个布尔值'''
        try:
            value = self.cf.getboolean(section, option)
            return value
        except Exception as e:
            print('取值报错：{}'.format(e))

    def get_str(self, section, option):
        '''从配置文件中获取一个字符串'''
        try:
            value = self.cf.get(section, option)
            return value
        except Exception as e:
            print('取值报错：{}'.format(e))

    def get_data(self, section, option):
        '''从配置文件里面获取一个元组  字典 列表等类型的数据'''
        try:
            value = self.cf.get(section, option)
            return value
        except Exception as e:
            print('取值报错：{}'.format(e))

if __name__ == '__main__':
    t = ReadConfig('case.config').get_data('RegisterCASE', 'case_id')
    print(t)

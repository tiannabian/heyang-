#coding: utf-8
#author = hewangtong
#date = 2020/5/3
import logging
from class_20200503.learn_conf import ReadConfig

class MyLog:
    '''这是一个日志类'''
    def __init__(self):
        self.logger_name = ReadConfig('log.conf').get_str('LOG', 'logger_name')
        self.logger_level = ReadConfig('log.conf').get_str('LOG', 'logger_level')
        self.formatter = ReadConfig('log.conf').get_str('LOG', 'formatter')
        self.stream_level = ReadConfig('log.conf').get_str('LOG', 'stream_level')
        self.file_name =  ReadConfig('log.conf').get_str('LOG', 'file_name')
        self.file_level = ReadConfig('log.conf').get_str('LOG', 'file_level')

    def my_log(self, level, msg):
        '''这是一个日志函数'''
        my_logger = logging.getLogger(self.logger_name)
        my_logger.setLevel(self.logger_level)

        formatter = logging.Formatter(self.formatter)
        ch = logging.StreamHandler()
        ch.setLevel(self.stream_level)  # 设置级别
        ch.setFormatter(formatter)  # 设置格式
        fh = logging.FileHandler(self.file_name, encoding='utf-8')
        fh.setLevel(self.file_level)  # 设置级别
        fh.setFormatter(formatter)  # 设置格式

        my_logger.addHandler(ch)
        my_logger.addHandler(fh)
        if level == 'DEBUG':
            my_logger.debug(msg)
        elif level == 'INFO':
            my_logger.info(msg)
        elif level == 'WARNING':
            my_logger.warning(msg)
        elif level == 'ERROR':
            my_logger.error(msg)
        else:
            my_logger.critical(msg)

        my_logger.removeHandler(ch)
        my_logger.removeHandler(fh)

    def debug(self, msg):
        self.my_log('DEBUG', msg)

    def info(self, msg):
        self.my_log('INFO', msg)

    def warning(self, msg):
        self.my_log('WARNING', msg)

    def error(self, msg):
        self.my_log('ERROR', msg)

    def critical(self,msg):
        self.my_log('CRITICAL', msg)

if __name__ == '__main__':
    MyLog().my_log('ERROR','我是python')
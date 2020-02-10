__author__ = '何旺彤'


import logging
from complete_test_api_test.common.project_path import log_path

class MyLog:

    def my_log(self, level, msg):
        #定义一个日志收集器并且还要设置级别
        my_logger = logging.getLogger('python14')
        my_logger.setLevel(('DEBUG'))
        #formatter是可以自己去配置的，指定输出渠道还要设置级别StreamHandler--控制台  FileHandler输出指定文件
        formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
        ch = logging.StreamHandler()
        ch.setLevel('INFO')#设置级别
        ch.setFormatter(formatter)#设置格式

        fh = logging.FileHandler(log_path, encoding = 'utf-8')#写入到指定文件
        fh.setLevel('INFO')#设置级别
        fh.setFormatter(formatter)#设置格式
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
        my_logger.removeHandler(fh)
        my_logger.removeHandler(ch)
        def debug(self, msg):
            self.my_log('DEBUG', msg)
        def info(self, msg):
            self.my_log('INFO', msg)

'''
if __name__ == '__main__':
    test_logger = MyLog().my_log('ERROR', '报错')
'''

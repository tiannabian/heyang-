#coding: utf-8
#author = hewangtong
#date = 2020/5/3
import logging


my_logger = logging.getLogger('python14')
my_logger.setLevel('INFO')

formatter = logging.Formatter('%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s')
ch = logging.StreamHandler()
ch.setLevel('INFO')   #设置级别
ch.setFormatter(formatter)   #设置格式
fh = logging.FileHandler('test.log', encoding='utf-8')
fh.setLevel('INFO')    #设置级别
fh.setFormatter(formatter)     #设置格式

my_logger.addHandler(ch)
my_logger.addHandler(fh)

my_logger.debug('用户名不能为空1')
my_logger.info('用户名不能为空2')
my_logger.warning('用户名不能为空3')
my_logger.error('用户名不能为空4')
my_logger.critical('用户名不能为空5')

my_logger.removeHandler(ch)
my_logger.removeHandler(fh)   #用完之后一定要记得移除掉


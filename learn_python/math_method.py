#coding: utf-8
#author = hewangtong
#date = 2020/4/25
#继承： 提高复用性

class MathMethod:
    '''这是一个数学类'''
    c = 10
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        '''加法'''
        return self.a+self.b+self.c

    @classmethod  #类函数
    def sub(cls):
        return cls.c+10

    @staticmethod  #静态函数
    def div():
        return 10



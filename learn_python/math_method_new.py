#coding: utf-8
#author = hewangtong
#date = 2020/4/25

from learn_python.math_method import MathMethod

class MathMethodNew(MathMethod):

    def __init__(self):
        self.a = 10
        self.b = 11

    def add(self):  #重新 override  重写特点：函数名一样（子类与父类），重写之后以重写为准
        return self.a+self.b+self.c

    def add_args(self, *args): #父类里面没有，子类里面有，叫做拓展函数
        sum = 0
        for i in args:
            sum = sum+i
        return sum

if __name__ == '__main__':
    res = MathMethodNew().add()
    print(res)




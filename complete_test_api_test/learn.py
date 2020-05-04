#coding: utf-8
#author = hewangtong
#date = 2020/3/29
#
'''
1. 冒泡排序法完成a = [18, 31, 13, 83, 35, 91, 10, 67, 14, 26, 37]的冒泡排序：
方法一：
a = [18, 31, 13, 83, 35, 91, 10, 67, 14, 26, 37]
a.sort()
print(a)
方法二：使用for循环
a = [18, 31, 13, 83, 35, 91, 10, 67, 14, 26, 26, 37]
for item in a:
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i], a[i+1] = a[i+1], a[i]
print(a)

2. 有1，2，3，4 四个数，能够组成多少个互不相同且无重复数字的三位数，都是什么呢？
count = 0
L = []#用来存储符合条件的数字
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and i != k:
                s = i*100+j*10+k
                count+=1
                L.append(s)
print(count)
print(L)

3. 写函数，判断用户传入的对象（字符串、列表、元组）的续航都是否大于5
def judge_len(*args):
    for item in args:
        if len(item)>5:
            print('参数:{},长度大于5'.format(item))
        else:
            print('输入错误')
judge_len('12367890', [1, 2, 3], (1, 2, 3))
4.写函数，检查传入列表的长度，如果大于2，那么仅仅保留前两个长度的内容，并将新内容返回
def judge_list(L):
    if isinstance(L, list):
        if len(L)>2:
            return L[:2]
        else:
            print('长度小于2')
    else:
        print('输入的不是列表')

print(judge_list([2, 4, 5, 87]))


5. 求0-7所能组成的奇数个数
count = 0
for i in range(0, 7777778):
    if '8' not in str(i) and '9' not in str(i):
        if i%2 != 0:
            count+=1
print(count)

6. 定义一个函数，传入一个字典和字符串，判断字符串是否为字典中的值，如果字符串不在字典中，则添加到字典中，并返回新的字典
import random
def get_key(d, s):
    while True:
        key = s+str(random.randint(1, 100))
        if key in d.keys():
            continue
        else:
            break
    return  key

def judge_dict(d, s):

        # 判断字符串是否为字典中的值，如果字符串不在字典中
        # d  字典
        # s   字符串
    key = get_key(d, s)
    if key not in d.values():
        d[key] = s
    return  d

d = {'python':'River'}
res = judge_dict(d, 'python')
print(res)

































































































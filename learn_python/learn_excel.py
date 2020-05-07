#coding: utf-8
#author = hewangtong
#date = 2020/4/25

# from openpyxl import load_workbook
#
# #打开workbook
# wb = load_workbook('D:\Lemon\learn_python\learn_python\learn_python.xlsx')
#
# #定位表单
# sheet = wb['Sheet1']
#
# sheet.cell(3,2,'这是李白的诗')  #行  列 value
# #sheet.cell(4,3).value='作者是李白'
#
# wb.save('learn_python.xlsx')  ##只要进行了单元格的更改就要去保存；如果这个文件不存在，就会创建这个文件然后去保存
# wb.close()


#读取所有行和所有列数据
# for i in range(1,sheet.max_row+1):
#     for j in range(1, sheet.max_column+1):
#         res = sheet.cell(row=i, column=j).value
#         if res != None:
#             print(res)
#读取excel的时候返回是None,那么有可能是空格
#填写了一个数据，没有读出来，可能是你没有保存，位置出错
#新建工作簿
# from openpyxl import workbook
#
# wb =workbook.Workbook()
# wb.save('python14.xlsx')

import pandas as pd

#读取全部数据
df = pd.read_excel('learn_python.xlsx')
#print(df.values)

#读取第一行数据
#print(df.iloc[0].values)   #返回值是列表

#读取多行数据，例如读取前两行数据
#print(df.iloc[[0,1]].values)

#读取指定行列，例如第一行第一列
#print(df.iloc[[0], [0]].values)

#
#print(df.index.values)
s = []
for i in df.index.values:
    s.append(df.iloc[[i],[1]].to_dict())
print(s)



























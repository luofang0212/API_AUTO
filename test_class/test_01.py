#!/usr/bin/env python
# -*- coding:utf-8 -*-

import xlrd
import pandas as pd

# 默认读第一个表单
df = pd.read_excel('testData_1.xlsx','工作表2')
# data = df.head()
# data = df.values
# print(data)
# df=pd.read_excel('lemon.xlsx')#这个会直接默认读取到这个Excel的第一个表单
data=df['case_id'].values  # 0表示第一行 这里读取数据并不包含表头，要注意哦！

print("读取指定行的数据：\n{0}".format(data))


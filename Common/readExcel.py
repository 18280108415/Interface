 #! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site: 
@software: PyCharm
@file: readExcel.py
@time: 2018/3/24 9:37
"""
import xlrd

class ReadExcel():
     def readExcel(fileName,SheetName="sheet1"):
         data = xlrd.open_workbook(fileName)
         table = data.sheet_by_name(SheetName)

         #获取总行数、总列数
         nrows = table.nrows
         print('hang')
         print(nrows)
         ncols = table.ncols
         print('lie')
         print(ncols)
         if nrows > 1:
             #获取第一列的内容，列表格式
             keys = table.row_values(0)
             print('keys')
             print(keys)

             listApiData = []
             #获取每一行的内容，列表格式
             for col in range(1,nrows):
                 values = table.row_values(col)
                 print('values')
                 print(values)
                 # keys，values这两个列表一一对应来组合转换为字典
                 api_dict = dict(zip(keys, values))
                 print("获取URL值")
                 url = api_dict.get('url')
                 payload = api_dict.get('payload')
                 header = api_dict.get('headers')
                 fc = api_dict.get('function')
                 print (api_dict.get('url'),payload,header,fc)
                 print('api_dict')
                 print(api_dict)
                 #返回list
                 listApiData.append(api_dict)
                 print("打印list")





             return listApiData
         else:
             print("表格未填写数据")
             return None

if __name__ == '__main__':

    s = ReadExcel.readExcel("../data/C1.2testCase1.xls", "C12testCase")

    print(s)












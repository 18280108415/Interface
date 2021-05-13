#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: case_01.py
@time: 2018/3/16 10:58
"""
import unittest
import requests
from ddt import ddt,data,unpack
from Common.SendRequests import SendRequest
from Common.readExcel import ReadExcel
import os
import  warnings
import re

#获取测试数据所在的目录
path = os.path.dirname(os.getcwd())+"\\data\\C1.2testCase1.xls"
#testData为list
testData = ReadExcel.readExcel(path, "C12testCase")

@ddt
class Test1(unittest.TestCase):

    def setUp(self):
        self.s = requests.session()

    def tearDown(self):
        pass
    #将list里每个值传参
    #list里每个值为字典类型数据

    @data(*testData)
    def test_yoyo_api(self,data):

        respon = SendRequest().send_request(self.s, data)
        #忽略warning
        warnings.simplefilter("ignore", ResourceWarning)
        #切割字符串取后面的部分
        expect_json = data["expected_json"]
        #print("expect_json")
        #print(expect_json)
        expected_status_code = data["expected_status_code"]
        #print(expected_status_code)
        expected_words = data["expected_words"]
        url = data["url"]
        #断言如果返回类型为json，则根据json 内容及status code来判断是否成功
        if data["response_type"] == 'json':
            self.assertIn(expect_json, str(respon.json()), url+"接口请求错误")
            self.assertEqual(expected_status_code,respon.status_code,url+"接口状态返回不正确")
        # 断言如果返回类型为html，则根据html内容 内容及status code来判断是否成功
        else:
            #通过正则表达式
            htms = re.findall(r"有声双语美文：.*?_沪江英语学习网", respon.text)  # 通过正则表达式 r"<a.*?>.*?</a>" 找到所有的数据并输出
            for item in htms:
                self.assertIn(expected_words, item, url+"接口请求错误")
                #通过状态断言
                self.assertEqual(expected_status_code, respon.status_code, url + "接口状态返回不正确")


if __name__ == '__main__':
    unittest.main()

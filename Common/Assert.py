'''time: 2018/5/8 10:58
author: fei.lee
this file is for assert'''

import unittest
from Common.SendRequests import SendRequest
from Common.readExcel import ReadExcel
import os
from Common.SendRequests import SendRequest

#获取测试数据所在的目录
path = os.path.dirname(os.getcwd())+"\\data\\C1.2testCase1.xls"

testData = ReadExcel.readExcel(path, "C12testCase")
print("test+66666666")
print(type(testData))


def assert_request():
    print("test0")
    print(testData[0])
    print(type(testData[0]))
    respon_type = testData[0]["response_type"]
    print(respon_type)
    print("test1")
    print(type(respon_type))

    print("test2")
    print (type(str(respon_type)))
    exp_json = testData[0]["expected_json"]
    print(exp_json)
    exp_words = testData[0]["expected_words"]
    print(exp_words)
    url =testData[0]["url"]
    print(url)
    headers = testData["headers"]
    print("打印headers")
    print(headers)
    print(type(headers))
    '''if api_data["data"] == "":
        dat = None'''




'''class AssertRequest():
    def assert_request(self, s, api_data):
        urllib3.disable_warnings()
        metho = api_data["method"]
        url = api_data["url"]
        if api_data["data"] == "":
            dat = None
        else:
            dat = eval(api_data["data"])
        if api_data["params"] == "":
            par = None
        else:
            par = eval(api_data["params"])
        if api_data["body"] == "":
            bod = None
        else:
            bod = api_data["body"]

        re = s.request(method=metho,url=url,data=bod,params=par,verify=False)

        return re'''
if __name__ == '__main__':
    assert_request()
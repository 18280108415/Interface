#! /usr/bin/env python
# -*- coding:utf-8 -*-

"""
@version: 1.0
@author: fky
@site:
@software: PyCharm
@file: run_main.py
@time: 2018/3/16 10:58
"""
import unittest
import time
import os
from Common.HTMLTestRunner_jpg import HTMLTestRunner

def run_case(dir = "testCases"):
    case_dir = os.path.dirname(os.getcwd()) + "\\" + dir

    print(case_dir)
    test_case = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(case_dir,pattern="test*.py",top_level_dir=None)
    return discover


if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    report_path = os.path.dirname(os.getcwd()) + "\\report\\" + current_time + '.html'  # 生成测试报告的路径
    fp = open(report_path, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"TestReport", description=u'interface test report',verbosity=2)
    runner.run(run_case())
    fp.close()
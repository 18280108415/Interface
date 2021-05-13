import requests
import json
import unittest
import re
import readExcel
import json
import os
path = os.path.dirname(os.getcwd())+"\\data\\C1.2testCase1.xls"

testData = readExcel.ReadExcel.readExcel(path, "C12testCase")
s = requests.session()
class UCTestCase(unittest.TestCase):
    def test_send_request(self):
        words= "'error': 0, 'msg': 'success'"
        res = s.request(method='post', url='https://fanyi.baidu.com/langdetect',
                   headers={'Content-Type':'application/x-www-form-urlencoded','charset':'UTF-8'},params={'query':'I miss you'}, verify=False)
        #返回的dict类型，str（）将dict转换成str
        re_json=str(res.json())
        #type()查看数据类型
        print(type(re_json))
        #re_json.dump()


        #print(re_json.dump())
        print(res.status_code)
        self.assertIn(words,re_json,'接口请求失败')
    def qtest_01_post(self):
       words = '学会感恩也就学会了快乐'

       res = s.request(method='get', url='http://www.hjenglish.com/new/p1261643/',
                   headers={'content-type': 'text/html', 'charset': 'utf-8'}, verify=False)
       #print(re.text)

       #正则提取里面的文字
       htms = re.findall(r"有声双语美文：.*?_沪江英语学习网", res.text) # 通过正则表达式 r"<a.*?>.*?</a>" 找到所有的数据并输出

       for item in htms:
           print(item)
       #self.assertEqual(200,res.status_code,"接口请求失败")
       self.assertIn(words,item,'接口请求失败')

       #self.assertIn(self,words,re.text)
       # print(re.status_code)
    def learn_test_02_get(self):
      re = s.request(method='post', url='https://fanyi.baidu.com/langdetect',
                   headers={'Content-Type': 'application/x-www-form-urlencoded', 'charset': 'UTF-8'},
                   params={'query': 'I miss you'}, verify=False)
      print(re.json())
      print(re.status_code)


if __name__ == '__main__':
    unittest.main()

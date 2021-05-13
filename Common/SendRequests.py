import requests

#author fei.lee
#data:2021.4.30
import readExcel
import urllib3

#加了后无warning 提示


class SendRequest():
    def send_request(self, s, api_data):
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

        return re
if __name__ == '__main__':
    s = requests.session()
    testData = readExcel.ReadExcel.readExcel("../data/C1.2testCase1.xls", "C12testCase")

    response = SendRequest().send_request(s,testData[0])
    print("testData")
    print(testData)
    print(testData[0])
    print(testData[1])
    print(testData[2])
    print(response)
    print("headers")





import requests

#get
'''headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36','Connection': 'keep-alive'}
r = requests.get('http://www.baidu.com/',headers=headers)
print(r.text)
print (r.encoding)
print(r.url)
print(r.content)
#解决r.text 乱码问题
print(r.content.decode('utf-8'))
print('test')
#print(r.raise_for_status())
print(r.status_code)'''

#post
url1= ("https://fanyi.baidu.com/langdetect")
payload = {'query':'I miss you'}
headers={'Content-Type':'application/x-www-form-urlencoded','charset':'UTF-8'}
'''r = requests.post("https://fanyi.baidu.com/langdetect", data=payload,header=headers)

print(r.text)
print(r.raise_for_status())'''

def send_post(url=None,data=None,header=None):
    r=requests.post(url, data,header)
    print(r.text)
    print(r.raise_for_status())
if __name__ == '__main__':
    send_post(url1,payload,headers)





'''response = requests.get("http://b-ssl.duitang.com/uploads/item/201707/20/20170720111208_EHX2K.jpeg")

print (response.content)
with open("love_img.jpeg","wb") as f:
     f.write(response.content)
     f.close()
#print(response.content)
#print(f.write(response.content).read_csv(f) )
print("Finish!")'''
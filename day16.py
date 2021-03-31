import requests
import json
from DBUtils import update
from DBUtils import select
# 请求数据并得到响应数据，使用post请求方式请求url地址
response = requests.post(url="http://192.168.1.244:8080/HKR/UserServlet?method=findAllStudent")
# 提取数据
response.encoding = "utf-8"
data = response.text
print(data)#打印响应数据的类型
d = json.loads(data)#将响应数据转换成字典
print(type(d),d)#遍历字典
#准备一张表
sql = "insert into reptilian1 values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#使用DBUtils然后将数据存储入到表中
for i in d:
    li1 = list(i.values())
    if(len(li1) == 14):
        li1.insert(2,"")
        update(sql,li1)
    if(len(li1) == 15):
        update(sql, li1)








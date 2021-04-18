import requests
from base.base_api import BaseApi
import json

API_HEADERS = {'content-type': 'application/x-www-form-urlencoded; charset=UTF-8'}
print(type(API_HEADERS))

data = {"token":"_oSEaZjbQ3DIzqcLJ80OXwCA8wcAAAAARg0AADsd2eC9lwMobPzrTzcLdOglOIOBEj32wuG9zZDEJZcSnywf4-IjlELHjP7GU6Dwlg"}
#
# # 对不存在的key赋值，就是增加key-value对
# data['数学'] = 93
# data['语文'] = 5.7
# data.update({'three': 3, 'four': 4})
# print(data)





url1= 'https://paymp.meituan.com/api/i/wallet/usercertify'

s = requests.session()
response = s.get(url=url1, params=data, headers=API_HEADERS)
print(response)

class tester(BaseApi):

    def build_custom_param(self, data):
        data['数学'] = 93
        data['语文'] = 5.7
        return data


# import yaml
#
# '''单个文件'''
# yaml.warnings({'YAMLLoadWarning':False})
# f=open('tester.yaml','r',encoding='utf-8')
# cfg=f.read()
# # print(cfg)
# d=yaml.load(cfg)
# print(d)
# f.close()



with open('test_demo.json','r',encoding='utf8')as fp:
    json_data = json.load(fp)



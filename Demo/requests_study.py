# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-09 11:26
# @File    : requests_study.py
# @Software: PyCharm
import urllib3
import urllib
import requests
import json

# response = requests.get("http://httpbin.org/get")
# print(response.text)
# print(response.reason)
demo = {"username": "admin", "password": "123456"}
demo1 = '{"username": "admin", "password": "123456"}'


# html = json.dumps(json.loads(demo1), indent=4)
# # html = json.dumps(demo, indent=4)
# print(html)


# def is_json(str_msg):
#     try:
#         json.loads(str_msg)
#         return True
#     except ValueError:
#         return False
#
#
# def better_json(msg):
#     if type(msg) is str:
#         if is_json(msg):
#             return json.dumps(json.loads(msg), indent=4)
#     elif type(msg) is dict:
#         return json.dumps(msg, indent=4)
#
#
# if __name__ == '__main__':
#     result = better_json(demo1)
#     print(result)

# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-02 15:38
# @File    : demo.py
# @Software: PyCharm
import functools
import random
import time
from urllib import request, parse
import ssl

import requests

import config

ssl._create_default_https_context = ssl._create_unverified_context
headers = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "User-Agent": random.choice(config.agents),
    # "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

params = parse.urlencode(
    [
        ("username", "admin"),
        ("password", "123")
    ]
)

localhost = "http://127.0.0.1:8000/login/"
demo_url = 'http://httpbin.org/get'
baidu_url = "https://www.baidu.com"


# req = request.Request(url=localhost, headers=headers, data=params)
# # req.add_header("User-Agent", random.choice(config.agents))
# with request.urlopen(req) as f:
#     data = f.read()
#     print('Status:', f.status, f.reason)
#     for k, v in f.getheaders():
#         print('%s: %s' % (k, v))
#     print("\n\n\nData:", data.decode('utf-8'))


# import telnetlib
#
# print('------------------------connect---------------------------')
# # 连接Telnet服务器
# try:
#     tn = telnetlib.Telnet('183.129.207.80', port='14512', timeout=20)
# except Exception:
#     print('该代理IP  无效')
# else:
#     print('该代理IP  有效')
#
# print('-------------------------end----------------------------')

# proxies = {
#     'http': '47.94.200.124:3128',
#     'https': '47.94.200.124:3128'
# }
#
# r = requests.post("http://127.0.0.1:8000/login/", data=None, proxies=proxies)
# print(r.status_code)
# print(r.text)

# def logging_tool(func):
#     def wrapper():
#         logging.warning('%s is running...' % func.__name__)
#         func()  # 把today当作参数传递进来，执行func()就相当于执行today()
#
#     return wrapper
#
#
# @logging_tool
# def today():
#     print(time.ctime())
#
#
# today()


# def logging_tool(level):
#     def decorator(func):
#         def wrapper():
#             if level == 'error':
#                 logging.error('%s is running...' % func.__name__)
#             elif level == 'warn':
#                 logging.warning('%s is running...' % func.__name__)
#             else:
#                 logging.info('%s is running...' % func.__name__)
#             func()
#
#         return wrapper
#
#     return decorator
#
#
# @logging_tool(level='warn')
# def today(name='admin'):
#     print('Hello, {}! Today is {}'.format(name, time.ctime()))
#
#
# today()


# def new_logging_tool(obj):
#     if isinstance(obj, str):  # 带参数的情况，参数类型为str
#         def decorator(func):
#             @functools.wraps(func)
#             def wrapper(*arg, **kwargs):
#                 if obj == 'error':
#                     logging.error('%s is running...' % func.__name__)
#                 elif obj == 'warn':
#                     logging.warn('%s is running...' % func.__name__)
#                 else:
#                     logging.info('%s is running...' % func.__name__)
#                 func()
#
#             return wrapper
#
#         return decorator
#     else:  # 不带参数的情况，参数类型为函数类型，即被装饰的函数
#         @functools.wraps(obj)
#         def wrapper(*args, **kwargs):
#             logging.info('%s is running...' % obj.__name__)
#             obj()
#
#         return wrapper
#
#
# @new_logging_tool
# def yesterday():
#     print('2018-05-24')
#
#
# yesterday()
#
#
# @new_logging_tool('warn')
# def today(name='devin'):
#     print('Hello, %s! Today is 208-05-25' % name)
#
#
# today()


# def debug():
#     import inspect
#     caller_name = inspect.stack()[1][3]
#     print("[DEBUG]: enter {}()".format(caller_name))
#
#
# def say_hello():
#     debug()
#     print("hello!")
#
#
# def say_goodbye():
#     debug()
#     print("goodbye!")
#
#
# if __name__ == '__main__':
#     say_hello()
#     say_goodbye()


# def debug(func):
#     def wrapper():
#         print("[DEBUG]: enter {}()".format(func.__name__))
#         return func()
#     return wrapper
#
# def say_hello():
#     print("hello!")
#
# say_hello = debug(say_hello)


def tools(func):
    def wrapper():
        print("正在被{}调用".format(func.__name__))
        return func()
    return wrapper


@tools
def say_hello():
    print("Hello world")


say_hello()

# # # -*- coding: utf-8 -*-
# # # @Author  : 翟会德
# # # @Time    : 2019-06-09 11:26
# # # @File    : requests_study.py
# # # @Software: PyCharm
# # import random
# # import requests
# # import json
# # from requests import Request, Session
# # from contextlib import closing
# #
# # import config
# #
# #
# # def is_json(str_msg):
# #     try:
# #         json.loads(str_msg)
# #         return True
# #     except ValueError:
# #         return False
# #
# #
# # def better_json(msg):
# #     if type(msg) is str:
# #         if is_json(msg):
# #             return json.dumps(json.loads(msg), indent=4)
# #     elif type(msg) is dict:
# #         return json.dumps(msg, indent=4)
# #
# #
# # # result = better_json(demo1)
# # # print(result)
# #
# # # base_url = "http://httpbin.org/get"
# # # test_url = "http://example.org"
# # # photo_url = "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1560074037993&di=7a5da8929f5e9acedba291248aa3a9d2&imgtype=0&src=http%3A%2F%2Fcdn4.freepik.com%2Fimage%2Fth%2F318-41747.jpg"
# # # headers = {
# # #     "User-Agent": random.choice(config.agents)
# # # }
# # # proxies = {
# # #     "http": "http://10.10.1.10:3128",
# # #     "https": "http://10.10.1.10:1080",
# # # }
# # # s = Session()
# # # response = s.get(test_url, headers=headers, proxies=proxies)
# # # print(response.text)
# #
# # # print(response.reason)
# # # print(response.headers)
# # # with open("./demo.jpg", "wb") as f:
# # #     response = s.get(url=photo_url, headers=headers, stream=True)
# # #     for i in response.iter_content(128):
# # #         f.write(i)
# #
# #
# # # def get_key_info(response, *args, **kwargs):
# # #     print(response.headers['Content-Type'])
# # #
# # #
# # # def main():
# # #     requests.get("https://api.github.com", hooks=dict(response=get_key_info))
# # #
# # #
# # # if __name__ == '__main__':
# # #     main()
# #
# #
# # # BASE_URL = "https://api.github.com"
# # #
# # #
# # # def construct_url(end_point):
# # #     return "/".join([BASE_URL, end_point])
# # #
# # #
# # # def basic_auth():
# # #     # 基本认证
# # #     response = requests.get(construct_url('user'), auth=("imoocdemo", "imoocdemo123"))
# # #     print(response.text)
# # #     # print(response.request.headers)
# #
# # import time
# # from functools import reduce
# #
# #
# # def performance(f):
# #     def fn(*args, **kw):
# #         t1 = time.time()
# #         r = f(*args, **kw)
# #         t2 = time.time()
# #         print('调用 %s()方法共用时：%fs' % (f.__name__, (t2 - t1)))
# #         return r
# #
# #     return fn
# #
# #
# # @performance
# # def factorial(n):
# #     return reduce(lambda x, y: x * y, range(1, n + 1))
# #
# #
# # print(factorial(10))
# import random
#
# # demo = [random.randint(1, 11) for _ in range(10)]
# # for i in demo:
# #     if i == 6:
# #         print("存在")
# #         break
# # else:
# #     print("不存在")
#
#
# from queue import Queue
# from threading import Thread
#
# # 用来表示终止的特殊对象
# _sentinel = object()
#
#
# # A thread that produces data
# def producer(out_q):
#     for i in range(10):
#         print("生产")
#         out_q.put(i)
#     out_q.put(_sentinel)
#
#
# # A thread that consumes data
# def consumer(in_q):
#     while True:
#         data = in_q.get()
#         if data is _sentinel:
#             in_q.put(_sentinel)
#             break
#         else:
#             print("消费", data)
#
#
# # Create the shared queue and launch both threads
# q = Queue()
# t1 = Thread(target=consumer, args=(q,))
# t2 = Thread(target=producer, args=(q,))
# t1.start()
# t2.start()


# from queue import Queue
#
# q = Queue()
# for i in range(1, 11):
#     q.put(i)
#
# for _ in range(5):
#     print(q.get())


from threading import Thread
from queue import Queue
import time
from selenium import webdriver

q = Queue()


def tools():
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    driver.maximize_window()
    time.sleep(3)
    driver.quit()


for _ in range(10):
    t = Thread(target=tools, args=())
    q.put(t)

while not q.empty():
    if q.qsize() == 5:
        break
    t = q.get()
    t.start()

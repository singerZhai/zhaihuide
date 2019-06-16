# # # -*- coding: utf-8 -*-
# # # @Author  : 翟会德
# # # @Time    : 2019-05-07 10:57
# # # @File    : first.py
# # # @Software: PyCharm
# # # !/user/bin/env python
# # # coding=utf-8
# import requests
# import datetime
# import time
# import threading
#
#
# class PerformanceTestTools(object):
#     times = []
#     error = []
#
#     def __my_request(self, url):
#         # myreq = PerformanceTestTools()
#         headers = {
#             'User-Agent': 'Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 4 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19'}
#
#         data = {"username": "admin", "password": "123456"}
#         r = requests.post(url, headers=headers, data=data)
#         ResponseTime = float(r.elapsed.microseconds) / 1000  # 获取响应时间，单位ms
#         self.times.append(ResponseTime)  # 将响应时间写入数组
#         if r.status_code != 200:
#             self.error.append("0")
#
#     def start_test(self, url, threads_count):
#         threads = []
#         start_time = datetime.datetime.now()
#         print("requests start time is {}".format(start_time))
#         think_time = 0.1
#         for i in range(threads_count):
#             t = threading.Thread(target=self.__my_request, args=(url,))
#             threads.append(t)
#
#         for t in threads:
#             time.sleep(think_time)
#             t.setDaemon(True)
#             t.start()
#         t.join()
#         end_time = datetime.datetime.now()
#         print("requests end time is {}".format(end_time))
#         time.sleep(3)
#         AverageTime = "{:.3f}".format(float(sum(self.times)) / float(len(self.times)))  # 计算数组的平均值，保留3位小数
#         print("平均响应时间 %s ms" % AverageTime)  # 打印平均响应时间
#         use_time = str(end_time - start_time)
#         hour = use_time.split(':').pop(0)
#         minute = use_time.split(':').pop(1)
#         second = use_time.split(':').pop(2)
#         all_time = float(hour) * 60 * 60 + float(minute) * 60 + float(second)  # 计算总的思考时间+请求时间
#         print("并发 %d 线程" % threads_count)
#         print("总时长：%f s" % (all_time - float(threads_count * think_time)))
#         print("failed ：%d " % self.error.count("0"))
#
#
# if __name__ == '__main__':
#     tools = PerformanceTestTools()
#     tools.start_test("http://0.0.0.0:8000/login/", 50)


# import time
# import asyncio
#
#
# # 定义异步函数
# async def hello():
#     # asyncio.sleep(1)
#     # asyncio.sleep(3)
#     print('Hello World:%s' % time.time())
#
#
# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())
#
#
# loop = asyncio.get_event_loop()
# if __name__ == '__main__':
#     run()


# import asyncio
# from aiohttp import ClientSession
#
# tasks = []
# url = "http://127.0.0.1:8000/login/"
#
#
# async def hello(url, data):
#     async with ClientSession() as session:
#         async with session.post(url, data=data) as response:
#             response = await response.read()
#             print(response)
#
#
# if __name__ == '__main__':
#     data = {
#         "username": "admin",
#         "password": "123456"
#     }
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(hello(url, data=data))


# import asyncio
# import time
# from aiohttp import ClientSession
#
# # async英文为异步的+io操作
# url = "http://127.0.0.1:8000/login/"
#
#
# async def req_get(url):
#     async with ClientSession() as session:
#         async with session.get(url) as response:
#             response = await response.read()
#     return response
#
#
# async def req_post(url, data):
#     async with ClientSession() as session:
#         async with session.post(url, data=data) as response:
#             response = await response.read()
#     return response
#
#
# if __name__ == '__main__':
#     data = {
#         'username': 'admin',
#         'password': '123456'
#     }
#     start = time.time()
#     # 方法可以创建一个事件循环,asyncio.BaseEventLoop。
#     # 协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务（task）对象。
#     # 所谓task对象是Future类的子类。保存了协程运行后的状态，用于未来获取协程的结果
#     loop = asyncio.get_event_loop()
#     # 需要处理的任务
#     tasks = [asyncio.ensure_future(req_post(url, data=data)) for i in range(20)]
#     # tasks = [loop.create_task(req_get(url)) for i in range(512)] 确定参数是协程的时候可以用这个
#     # 将协程注册到事件循环，并启动事件循环
#     # loop.run_until_complete(asyncio.gather(*tasks))
#     loop.run_until_complete(asyncio.wait(tasks))
#     for task in tasks:
#         print(task)
#         print('Task ret: ', task.result())
#     print('TIME: ', time.time() - start)


# import asyncio
# import time
#
#
# @asyncio.coroutine
# def hello():
#     print("Hello World", time.time())
#     yield from asyncio.sleep(1)
#     print("Hello again!", time.time())
#
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()


# import threading
# import asyncio
#
#
# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
#
#
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio
#
#
# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#     # Ignore the body, close the socket
#     writer.close()
#
#
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# import asyncio
# import time
#
#
# now_time = lambda :time.time()
#
#
# async def main():
#     print("Hello ...", now_time())
#     await asyncio.sleep(3)
#     print("...World", now_time())
#
#
# asyncio.run(main())


# import time
# import requests
# from concurrent.futures import ThreadPoolExecutor
#
# NUMBERS = range(12)
# URL = 'http://httpbin.org/get?a={}'
#
#
# def fetch(a):
#     r = requests.get(URL.format(a))
#
#     return r.json()['args']['a']
#
#
# start = time.time()
# with ThreadPoolExecutor(max_workers=3) as executor:
#     for num, result in zip(NUMBERS, executor.map(fetch, NUMBERS)):
#         print('fetch({}) = {}'.format(num, result))
#
# print('Use requests+ThreadPoolExecutor cost: {}'.format(time.time() - start))


# import requests
# import time
# import asyncio
#
# data = {
#     "username": "admin",
#     "password": "123456"
# }
#
#
# # 创建一个异步函数
# async def task_func():
#     await asyncio.sleep(1)
#     resp = requests.post('http://127.0.0.1:8000/login/', data=data)
#     print('2222222', time.time(), resp.text)
#
#
# async def main(loop):
#     # loop = asyncio.get_event_loop()  # 获取全局轮训器
#     task = loop.create_task(task_func())  # 在全局轮训器加入协成，只有加入全局轮训器才能被监督执行
#     await asyncio.sleep(2)  # 等待两秒为了不要立即执行event_loop.close()，项目中event_loop应该是永不停歇的
#     print('11111111111', time.time())
#
#
# event_loop = asyncio.get_event_loop()
#
# try:
#     event_loop.run_until_complete(main(event_loop))
# finally:
#     event_loop.close()  # 当轮训器关闭以后，所有没有执行完成的协成将全部关闭


# import time
# import asyncio
#
#
# # 定义异步函数
# async def hello():
#     await asyncio.sleep(1)
#     print('Hello World:%s' % time.time())
#
#
# def run():
#     for i in range(5):
#         loop.run_until_complete(hello())
#
#
# loop = asyncio.get_event_loop()
# if __name__ == '__main__':
#     run()


# coding:utf-8
# import time, asyncio, aiohttp
#
# url = 'http://127.0.0.1:8000/login/'
#
#
# async def hello(url, semaphore):
#     async with semaphore:
#         async with aiohttp.ClientSession() as session:
#             async with session.get(url) as response:
#                 return await response.read()
#
#
# async def run():
#     semaphore = asyncio.Semaphore(10)  # 限制并发量为500
#     to_get = [hello(url.format(), semaphore) for _ in range(100)]  # 总共1000任务
#     await asyncio.wait(to_get)
#
#
# if __name__ == '__main__':
#     # loop = asyncio.get_event_loop()
#     # loop.run_until_complete(run())
#     # loop.close()
#     print(asyncio.Semaphore(100))


# import asyncio
# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
#
# async def demo(count):
#     await asyncio.sleep(3)
#     for _ in range(count):
#         driver = webdriver.Firefox()
#         driver.maximize_window()
#         driver.implicitly_wait(10)
#         driver.get("http://cal.apple886.com/")
#         # driver.find_element(By.CSS_SELECTOR, "#simple1")
#         driver.quit()
#
#
# start_time = time.time()
#
#
# first = demo(2)
# second = demo(5)
# loop = asyncio.get_event_loop()
# # task = asyncio.ensure_future(first_scene)
# # task.add_done_callback(callback)
# # loop.run_until_complete(task)
#
# tasks = [
#     asyncio.ensure_future(first),
#     asyncio.ensure_future(second)
# ]
#
# loop.run_until_complete(asyncio.wait(tasks))
#
# print("end")
# print("use time is: ", time.time() - start_time)
import asyncio
import time
import requests
from selenium import webdriver

# async def driver_test(url, times):
#     await asyncio.sleep(1)
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get(url)
#     driver.implicitly_wait(10)
#     await time.sleep(times)
#     driver.quit()
# await asyncio.sleep(time)


# url = ["https://segmentfault.com/p/1210000013564725",
#        "https://www.jianshu.com/p/83badc8028bd",
#        "https://www.baidu.com/"]

# async def other_test(url, time):
#     await driver_test(url, time)
#
# url = "https://www.baidu.com/"
#
# times = [5, 10]
#
# loop = asyncio.get_event_loop()
# task = [asyncio.ensure_future(other_test(url, i)) for i in times]
# start = time.time()
# loop.run_until_complete(asyncio.wait(task))
# all_times = time.time() - start
# print("all_times: ", all_times)
# loop.close()
#
# import threading
#
# url = "https://www.baidu.com/"
#
#
# def driver_test(times):
#     driver = webdriver.Firefox()
#     driver.maximize_window()
#     driver.get(url)
#     driver.implicitly_wait(10)
#     time.sleep(times)
#     driver.quit()
#
#
# threads = [threading.Thread(target=driver_test, args=(i,)) for i in range(5, 10)]
#
# for thread in threads:
#     print("开始", thread.name)
#     thread.start()
#     # print()
# thread.join()
# print("end")

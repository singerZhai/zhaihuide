# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-27 19:49
# @File    : demo.py
# @Software: PyCharm
# import os
# import time
#
# while True:
#     os.system("adb shell dumpsys meminfo com.baidu.fsg.rimdemo")
#     time.sleep(0.5)

# 需要先安装 aiohttp: pip install aiohttp
import asyncio
import datetime
import aiohttp  # 可以理解为一个支持异步 I/O 的 requests


async def fetch_page(url):
    async with aiohttp.ClientSession() as session:
        async with session.post(url) as response:
            return await response.json()


# if __name__ == '__main__':
#     loop = asyncio.get_event_loop()
#     result = loop.run_until_complete(fetch_page('http://httpbin.org/post'))  # httpbin 这个网站能测试 http 请求和响应的各种信息
#     print(f"{result.get('headers')}")
#     print(f"Args: {result.get('args')}")
#     loop.close()

# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-07 13:32
# @File    : proxy.py
# @Software: PyCharm
import json
import random
from time import sleep
from telnetlib import Telnet
import requests
from lxml import etree

base_url = "https://www.kuaidaili.com/free/inha/{}/"
# checkUrl = 'http://httpbin.org/ip'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
}

proxy = []
for i in range(1, 2):
    try:
        response = requests.get(url=base_url.format(i), headers=headers)
    except Exception:
        print("failed")
        continue
    select = etree.HTML(response.text)
    ip_list = select.xpath("//*[@data-title='IP']/text()")
    port_list = select.xpath("//*[@data-title='PORT']/text()")
    for ip, port in zip(ip_list, port_list):
        res = ip + ":" + port
        try:
            # TODO:连接Telnet服务器，验证代理IP是否有效
            tn = Telnet(ip, port=port, timeout=1)
        except Exception:
            # print('该代理IP  无效')
            pass
        else:
            proxy.append(res)
            # print('该代理IP  有效: ', ip)
print("共获取 {} 个有效代理IP".format(len(proxy)))
with open("./proxies.txt", "w", encoding="utf-8") as f:
    for i in proxy:
        f.write(i + "\n")

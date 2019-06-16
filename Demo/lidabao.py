# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-31 13:09
# @File    : lidabao.py
# @Software: PyCharm
import requests
import unittest


class TestDemo(unittest.TestCase):

    def setUp(self):
        self.session = requests.session()

    def test_demo(self):
        url = "自己的url"
        data = "自己的参数（字典）例：{'username': 'admin', 'password': '123456'}"
        response = self.session.post(url, data)
        # 将返回信息转化为json,消息体中有状态码和msg
        result = response.json()
        self.assertEqual('200', result['对应状态码的key'])
        self.assertEqual("预期msg", result['对应msg的key'])

    def tearDown(self):
        self.session.close()

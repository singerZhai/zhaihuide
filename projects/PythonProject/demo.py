import requests
import unittest
import json
import random
import string
import time


class TestDemo(unittest.TestCase):

    def random_str(self, length):
        random_str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
        random_str = ''.join(random_str_list)
        return random_str

    def setUp(self):
        self.loginUrl = 'http://127.0.0.1/login'
        self.sign_in_url = 'http://127.0.0.1/sign_in'
        self.loginData = {
            'username': 'admin',
            'password': '123456'
        }

    def test_login(self):
        while True:
            r = requests.post(url=self.loginUrl, data=self.loginData)
            res = r.json()
            result = json.dumps(res, ensure_ascii=False)
            print(result)
            time.sleep(1)

    def test_sign_in(self):
        while True:
            sign_in_data = {
                'username': self.random_str(10),
                'password': self.random_str(6)
            }
            r = requests.post(url=self.sign_in_url, data=sign_in_data)
            res = r.json()
            result = json.dumps(res, ensure_ascii=False)
            print(result)
            time.sleep(1)

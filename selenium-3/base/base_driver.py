# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-15 00:18
# @File    : base_driver.py
# @Software: PyCharm
from selenium import webdriver


class BaseDriver(object):

    driver = None

    @classmethod
    def base_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.maximize_window()
            cls.driver.get("http://127.0.0.1:8000/login/")
            # cls.driver.get("http://127.0.0.1:8000/sign_in/")
            # cls.driver.get("https://www.masstea.com/")
            cls.driver.implicitly_wait(10)
        return cls.driver

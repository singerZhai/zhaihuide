# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-15 15:31
# @File    : test_login.py
# @Software: PyCharm
import time
import unittest
from base.base_driver import BaseDriver
import pages


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("start")
        cls.driver = BaseDriver.base_driver()
        cls.page = pages.login_page(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(3)
        cls.driver.quit()

    def test_login(self):
        self.page.input_username("admin")
        self.page.input_password("123456")
        self.page.click_login_btn()

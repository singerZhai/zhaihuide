# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-15 18:04
# @File    : test_sign_in.py
# @Software: PyCharm
import time
import unittest
import pages
from base.base_driver import BaseDriver


class TestSignIn(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = BaseDriver.base_driver()
        self.sign_in_page = pages.sign_in_page(self.driver)

    def tearDown(self) -> None:
        time.sleep(3)
        self.driver.quit()

    def test_sign_in(self):
        self.sign_in_page.input_username('admin')
        self.sign_in_page.input_password('123456')
        self.sign_in_page.click_sign_in_btn()

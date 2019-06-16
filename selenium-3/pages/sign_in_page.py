# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-15 17:51
# @File    : sign_in_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By

from base.base import BaseAction


class SignInPage(BaseAction):

    username = By.NAME, "username"
    password = By.NAME, "password"
    sign_in_btn = By.XPATH, "//*[@value='注册']"

    def input_username(self, username):
        self.send_keys(self.username, username)

    def input_password(self, password):
        self.send_keys(self.password, password)

    def click_sign_in_btn(self):
        self.click(self.sign_in_btn)

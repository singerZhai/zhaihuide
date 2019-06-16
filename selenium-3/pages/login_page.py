# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-15 15:24
# @File    : login_page.py
# @Software: PyCharm
from selenium.webdriver.common.by import By
from base.base import BaseAction


class LoginPage(BaseAction):

    username = By.NAME, "username"
    password = By.NAME, "password"
    login_btn = By.XPATH, "//*[@value='登录']"

    def input_username(self, username):
        self.send_keys(self.username, username)

    def input_password(self, password):
        self.send_keys(self.password, password)

    def click_login_btn(self):
        self.click(self.login_btn)

# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-06-14 23:38
# @File    : base.py
# @Software: PyCharm
from selenium.webdriver.support.wait import WebDriverWait


class BaseAction(object):

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, location, timeout=10.0, poll=0.1):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
        return wait.until(lambda x: x.find_element(*location))

    def find_elements(self, location, timeout=10.0, poll=0.1):
        wait = WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll)
        return wait.until(lambda x: x.find_elements(*location))

    def click(self, location):
        self.find_element(location).click()

    def send_keys(self, location, text):
        ele = self.find_element(location)
        ele.clear()
        ele.send_keys(text)

    def get_ele_text(self, location):
        ele = self.find_element(location)
        return ele.text

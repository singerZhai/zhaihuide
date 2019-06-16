# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-24 21:38
# @File    : demo.py
# @Software: PyCharm
import subprocess

status = subprocess.run(["ls", "-a"], shell=False)
print(status)

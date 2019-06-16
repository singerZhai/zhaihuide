# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-30 17:09
# @File    : interface.py
# @Software: PyCharm
import random
import string
from json import JSONDecodeError
from threading import Thread
import requests
import config
import json


def write_str(length):
    str_list = [random.choice(string.ascii_letters + string.digits) for _ in range(length)]
    res_str = ''.join(str_list)
    with open("./str.txt", "w", encoding="utf-8") as f:
        f.write(res_str)


def chinese(length):
    # val = random.randint(0x4e00, 0x9fbf)
    # res = chr(val)
    res_list = [chr(random.randint(0x4e00, 0x9fbf)) for _ in range(length)]
    res = ''.join(res_list)
    with open("./中文.txt", "w", encoding="utf-8") as f:
        f.write(res)


def random_materiel_name(length=3):
    random_str_list = [random.choice(string.digits + string.ascii_letters) for _ in range(length)]
    random_str = ''.join(random_str_list)
    return random_str


url_change = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/edit"
url_list = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/list"
url_add = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/add"
url_detail = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/detail"
url_delete = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/materiel/delete"
url_content = "http://cp01-fintechqa-bj-01.epc.baidu.com:8567/cifsman/marketchannel/content"

headers = {
    'cookie': config.cookie,
    'User-Agent': random.choice(config.agents)
}


def json_tools(msg):
    try:
        res = json.dumps(json.loads(msg), indent=4, ensure_ascii=False)
        return res
    except JSONDecodeError as e:
        print("解析失败: ", msg)


def materiel(url, data=None):
    response = requests.post(url=url, json=data, headers=headers)
    return response.text


def materiel_create(name):
    data_add = {
        "marketChannelId": "MESSAGE",
        # "marketChannelId": 1,
        "materielContent": '{"desireAwake":"想要提升学历、获取就业机会，","corePoint":"现参与推荐有礼活动，邀请好友购买保险最低可得52元，多邀多得","rightsBenefits":"还不快来参与。","link":"点击<link>"}',
        "materielDescribe": "interface_create",
        "materielLink": "https://www.taobao.com",
        "materielName": "{}".format(name),
        "materielText": "想要提升学历、获取就业机会，现参与推荐有礼活动，邀请好友购买保险最低可得52元，多邀多得还不快来参与。点击<link>  回TD退订",
        "materielUnsubscribe": "true",
        "useMaterielTemplate": "true"
    }
    response = materiel(url_add, data_add)
    print(json_tools(response))


def materiel_delete(id):
    data_delete = {
        "materielId": "MTR0000{}".format(id)
    }
    response = materiel(url_delete, data_delete)
    print(json_tools(response))


def materiel_change(id):
    data_change = {
        "marketChannelId": "MESSAGE",
        "materielName": "interface-change-1",
        "materielDescribe": "interface-change",
        "useMaterielTemplate": "true",
        "materielLink": "https://www.baidu.com",
        "materielUnsubscribe": "true",
        "materielText": "据说人手都有一张信用卡？马上办卡，获取火箭粉丝专属特权，现在申请就送799元拉杆箱。点击<link>  回TD退订",
        "materielContent": "{\"desireAwake\":\"据说人手都有一张信用卡？\",\"corePoint\":\"马上办卡，获取火箭粉丝专属特权，\",\"rightsBenefits\":\"现在申请就送799元拉杆箱。\",\"link\":\"点击<link>\"}",
        "materielId": "MTR0000{}".format(id)
    }
    response = materiel(url_change, data_change)
    print(json_tools(response))


def materiel_detail(id):
    data_detail = {
        "materielId": "MTR0000{}".format(id)
    }
    response = materiel(url_detail, data_detail)
    print(json_tools(response))


def materiel_list(page):
    data_list = {
        "pageNo": '{}'.format(page),
        "pageSize": 10
    }
    response = materiel(url_list, data_list)
    print(json_tools(response))


def materiel_content():
    data_content = {
        "contentType": "MATERIEL_TEMPLATE"
    }
    response = materiel(url_content, data_content)
    print(json_tools(response))


if __name__ == '__main__':
    # for i in range(3):
    #     t = Thread(target=materiel_create, args=(i,))
    #     t.start()
    # materiel_create("弄啥嘞")
    # materiel_list(1)
    # materiel_delete("")
    materiel_detail(2236)
    # materiel_change(2236)
    # chinese(500)
    # write_str(1024)
    # materiel_content()

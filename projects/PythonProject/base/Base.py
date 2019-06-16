from mysql.MySQL import OpenDB
import random
import string
import json


class MysqlUtil():

    def select_sql(self, sql):
        with OpenDB() as f:
            f.execute(sql)
            result = f.fetchall()
            return result

    def insert_sql(self, sql):
        with OpenDB() as f:
            f.execute(sql)

    def update_sql(self, sql):
        with OpenDB() as f:
            f.execute(sql)


class Base(object):

    def userToken(self):
        str_list = [random.choice(string.ascii_letters + string.digits) for i in range(30)]
        user_token = ''.join(str_list)
        return user_token

    def json_response(self, str):
        res = json.dumps(str, ensure_ascii=False)
        return res


class Conf():

    def __init__(self):
        self.code_msg = {
            '200': {
                'code': '200',
                'msg': 'Success',
                'userToken': Base().userToken()
            },
            '201': {
                'code': '200',
                'msg': '注册成功'
            },
            '0': {
                'code': '0',
                'msg': '参数不合法'
            },
            '400': {
                'code': '400',
                'msg': '系统繁忙，请稍候重试'
            },
            '01': {
                'code': '01',
                'msg': '密码错误'
            },
            '02': {
                'code': '02',
                'msg': '用户名已存在'
            },
            '03': {
                'code': '03',
                'msg': '用户未注册'
            },
            '04': {
                'code': '04',
                'msg': '密码不能为空'
            },
            '05': {
                'code': '05',
                'msg': '用户名不能为空'
            },
            '06': {
                'code': '06',
                'msg': '密码不能为空'
            }
        }

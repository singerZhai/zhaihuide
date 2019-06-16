import flask
from base.Base import *
server = flask.Flask(__name__)


class Util():

    def __init__(self):
        self.mysql = MysqlUtil()
        self.conf = Conf().code_msg
        __all_user = self.mysql.select_sql("select username,password from users_data")
        __new_list = list()
        for i in __all_user:
            for j in i.values():
                __new_list.append(j)
        self.all_data = dict(zip(__new_list[0::2], __new_list[1::2]))


@server.route('/sign_in', methods=['post'])
def sign_in():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')
    print({'username': username, 'password': password})
    util = Util()
    if username is None:
        return json.dumps(util.conf['0'], ensure_ascii=False)
    if password is None:
        return json.dumps(util.conf['0'], ensure_ascii=False)
    if username == "":
        return json.dumps(util.conf['05'], ensure_ascii=False)
    if username not in util.all_data:
        if password != "":
            try:
                util.mysql.insert_sql("insert into users_data(username,`password`) values('%s','%s')" % (username, password))
            except Exception:
                raise None
            return json.dumps(util.conf['201'], ensure_ascii=False)
        return json.dumps(util.conf['06'], ensure_ascii=False)
    return json.dumps(util.conf['02'], ensure_ascii=False)


@server.route('/login', methods=['post', 'get'])
def login():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')
    print({'username': username, 'password': password})
    util = Util()
    if username is None:
        return json.dumps(util.conf['0'], ensure_ascii=False)
    if password is None:
        return json.dumps(util.conf['0'], ensure_ascii=False)
    if username == "":
        return json.dumps(util.conf['05'], ensure_ascii=False)
    if password == "":
        return json.dumps(util.conf['06'], ensure_ascii=False)
    if username in util.all_data:
        if password == util.all_data[username]:
            return json.dumps(util.conf['200'], ensure_ascii=False)
        return json.dumps(util.conf['01'], ensure_ascii=False)
    return json.dumps(util.conf['03'], ensure_ascii=False)


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=80, debug=True)

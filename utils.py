import json

import pymysql

import app


def assert_common(self, response, http_code, success, code, message):
    self.assertEqual(http_code, response.status_code)  # 断言响应状态码
    self.assertEqual(success, response.json().get('success'))  # 断言success
    self.assertEqual(code, response.json().get('code'))  # 断言code
    self.assertIn(message, response.json().get('message'))  # 断言message


def read_login_date():
    filename = app.BASE_DIR + '/data/login_data.json'
    with open(filename, 'r', encoding='utf-8')as f:
        jsondata = json.load(f)
        dict_list = list()
        # print(jsondata)
        for dict in jsondata:
            mobile = dict.get('mobile')
            password = dict.get('password')
            http_code = dict.get('http_code')
            success = dict.get('success')
            code = dict.get('code')
            message = dict.get('message')
            dict_list.append((mobile, password, http_code,
                              success, code, message))
        print(dict_list)
        return dict_list


def read_add_emp_data():
    filename = app.BASE_DIR + '/data/employee.json'
    with open(filename, encoding='utf-8')as f:
        jsondata = json.load(f)
        add_emp_list = list()
        # 获取add_emp的数据
        add_emp_data = jsondata.get('add_emp')
        # 获取要传入的具体数值
        username = add_emp_data.get("username")
        password = add_emp_data.get("password")
        http_code = add_emp_data.get("http_code")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        # 将数据加入列表
        add_emp_list.append((username, password, http_code, success, code, message))
    print(add_emp_list)
    return add_emp_list


def read_query_emp_data():
    filename = app.BASE_DIR + '/data/employee.json'
    with open(filename, encoding='utf-8')as f:
        jsondata = json.load(f)
        query_emp_list = list()
        # 获取query_emp的数据
        query_emp_data = jsondata.get('query_emp')
        # 获取要传入的具体数值
        http_code = query_emp_data.get("http_code")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        # 将数据加入列表
        query_emp_list.append((http_code, success, code, message))
    print(query_emp_list)
    return query_emp_list


def read_modify_emp_data():
    filename = app.BASE_DIR + '/data/employee.json'
    with open(filename, encoding='utf-8')as f:
        jsondata = json.load(f)
        modify_emp_list = list()
        # 获取add_emp的数据
        modify_emp_data = jsondata.get('modify_emp')
        # 获取要传入的具体数值
        username = modify_emp_data.get("username")
        password = modify_emp_data.get("password")
        http_code = modify_emp_data.get("http_code")
        success = modify_emp_data.get("success")
        code = modify_emp_data.get("code")
        message = modify_emp_data.get("message")
        # 将数据加入列表
        modify_emp_list.append((username, password, http_code, success, code, message))
    print(modify_emp_list)
    return modify_emp_list


def read_remove_emp_data():
    filename = app.BASE_DIR + '/data/employee.json'
    with open(filename, encoding='utf-8')as f:
        jsondata = json.load(f)
        remove_emp_list = list()
        # 获取query_emp的数据
        remove_emp_data = jsondata.get('remove_emp')
        # 获取要传入的具体数值
        http_code = remove_emp_data.get("http_code")
        success = remove_emp_data.get("success")
        code = remove_emp_data.get("code")
        message = remove_emp_data.get("message")
        # 将数据加入列表
        remove_emp_list.append((http_code, success, code, message))
    print(remove_emp_list)
    return remove_emp_list


class DButils:
    def __init__(self, host='182.92.81.159', user='readuser',
                 password='iHRM_user_2019', database='ihrm'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    # __enter__和__exit__是一对魔法方法，和with一起用，用于获取和关闭游标
    #如：with DButils as db:
    #db可以用来执行sql语句，db相当于cursor
    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    read_remove_emp_data()

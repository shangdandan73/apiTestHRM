import logging
import unittest

import pymysql

import app
import utils
from api.emp_api import EmpApi
from parameterized import parameterized


class TestIHRMEmp(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmpApi()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @parameterized.expand(utils.read_add_emp_data)
    def test01_add_emp(self, username, password, http_code, success, code, message):
        '''添加员工函数'''
        # 发送请求
        response = self.emp_api.add_emp(username, password)
        # 获取响应json信息
        jsondata = response.json()
        # 打印返回的response
        logging.info('打印返回的response:{}'.format(jsondata))
        # 断言
        utils.assert_common(self, response, http_code, success, code, message)

        # 获取员工ID并保存到全局变量
        app.EMP_ID = jsondata.get('data').get('id')
        logging.info(app.EMP_ID)

    @parameterized.expand(utils.read_query_emp_data)
    def test02_query_emp(self, http_code, success, code, message):
        '''查询员工信息'''
        # 发送查询请求
        response = self.emp_api.query_emp()
        # 打印查询响应结果
        logging.info('查询响应信息为：{}'.format(response.json()))
        # 断言
        utils.assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(utils.read_modify_emp_data)
    def test03_modify_emp(self, username, password, http_code, success, code, message):
        '''修改员工测试方法'''
        # 发送修改员工接口请求
        response = self.emp_api.modify_emp(username, password)
        # 打印响应json报文
        jsondata = response.json()
        logging.info('修改员工信息的json数据为：{}'.format(jsondata))
        # 查看数据库是否增加成功
        with utils.DButils()as db:
            sql = 'select username from bs_user where id={}'.format(app.EMP_ID)
            db.execute(sql)
            result = db.fetchone()[0]
            logging.info('数据库查询到的username为：{}'.format(result))
        self.assertEqual(username, result)
        # 断言
        utils.assert_common(self, response, http_code, success, code, message)

    @parameterized.expand(utils.read_remove_emp_data)
    def test04_remove_emp(self, http_code, success, code, message):
        '''删除员工测试方法'''
        # 调用删除请求方法
        response = self.emp_api.remove_emp()
        # 获取删除员工响应json信息
        jsondata = response.json()
        logging.info('删除员工的响应信息：{}'.format(jsondata))
        # 断言
        utils.assert_common(self, response, http_code, success, code, message)


if __name__ == '__main__':
    unittest.main()

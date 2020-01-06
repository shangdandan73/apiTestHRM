import logging
import unittest
import utils

from api.login_api import LoginApi


class Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test01_login_success(self):
        response = self.login_api.login("13800000002", '123456')
        # 获取响应信息中的json
        jsondata = response.json()
        logging.info('响应信息中的json为：{}'.format(jsondata))
        # 响应内容断言
        utils.assert_common(self,response,200,True,10000,'操作成功')
        # self.assertEqual(200, responses.status_code)  # 断言响应状态码
        # self.assertEqual(True, jsondata.get('success'))  # 断言success
        # self.assertEqual(10000, jsondata.get('code'))  # 断言code
        # self.assertIn('操作成功', jsondata.get('message'))  # 断言message

    def test02_user_not_exist(self):
        response = self.login_api.login('13900000020','123456')
        #获取响应信息
        jsondata = response.json()
        logging.info('响应为：{}'.format(jsondata))
        #断言
        utils.assert_common(self,response,200,False,20001,'用户名或密码错误')

    def test03_password_error(self):
        response = self.login_api.login('13800000002','error')
        #获取响应信息
        jsondata = response.json()
        logging.info('响应为：{}'.format(jsondata))
        #断言
        utils.assert_common(self,response,200,False,20001,'用户名或密码错误')



if __name__ == '__main__':
    unittest.main()
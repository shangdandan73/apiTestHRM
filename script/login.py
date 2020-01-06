import logging
import unittest

import app
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

    def test_login_success(self):
        response = self.login_api.login("13800000002", '123456')
        # 获取响应信息中的json
        jsondata = response.json()
        logging.info('响应信息中的json为：{}'.format(jsondata))
        # 响应内容断言
        utils.assert_common(self,response,200,True,10000,'操作成功')

        #获取响应内容中的令牌
        token = jsondata.get('data')

        app.HEADERS['Authorization']='Bearer '+token
        logging.info('保存令牌后的Headers：{}'.format(app.HEADERS))



if __name__ == '__main__':
    unittest.main()
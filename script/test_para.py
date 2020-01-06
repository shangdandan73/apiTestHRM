import logging
import unittest

from api.login_api import LoginApi
from parameterized.parameterized import parameterized

from utils import assert_common, read_login_date


class TestIHRMLogin(unittest.TestCase):

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

    @parameterized.expand(read_login_date)
    def test_login_success(self,mobile,password,http_code,success,code,message):
        response = self.login_api.login(mobile, password)
        # 获取响应信息中的json
        jsondata = response.json()
        logging.info('响应信息中的json为：{}'.format(jsondata))
        # 响应内容断言
        assert_common(self, response, http_code, success, code, message)


if __name__ == '__main__':
    unittest.main()
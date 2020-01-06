import time
import unittest
import app
from script.ihrm_emp import TestIHRMEmp


# 初始化测试套件
from script.login import Login
from script.test_para import TestIHRMLogin
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()
# 将用例加入套件
suite.addTest(unittest.makeSuite(Login))
suite.addTest(unittest.makeSuite(TestIHRMEmp))
# suite.addTest(unittest.makeSuite(TestIHRMLogin))

# 设置测试报告文件路径并加时间戳
filename = app.BASE_DIR + '/report/report_{}.html'.format(time.strftime('%Y%m%d-%H%M%S'))
# 使用HTMLTestRunner执行测试用例，生成测试报告
with open(filename, 'wb')as f:
    # 实例化HtmlTestRunner对象
    runner = HTMLTestRunner(stream=f, verbosity=2,
                            title='IHRM接口测试报告',
                            description='tester:dandan')

    runner.run(suite)

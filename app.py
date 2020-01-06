# 编写初始化日志的函数
import logging.handlers
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
HOST = "http://182.92.81.159"
HEADERS = {"Content-Type":"application/json"}
EMP_ID = 0


def init_log():
    # 创建日志器
    logger = logging.getLogger()
    # 修改日志等级
    logger.setLevel(logging.INFO)
    # 创建处理器
    # 控制台处理器
    sh = logging.StreamHandler()
    # 文件处理器
    filename = BASE_DIR + '/log/ihrm.log'
    fh = logging.handlers.TimedRotatingFileHandler(filename=filename, when='S', interval=4, backupCount=4)
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)
    # 将格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)
    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(fh)

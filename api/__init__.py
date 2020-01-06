import app
import logging

#调用初始化日志函数
app.init_log()

if __name__ == '__main__':
    logging.info('测试日志初始化是否成功')
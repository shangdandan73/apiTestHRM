import app
import requests


class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers =app.HEADERS

    def login(self,mobile,password):
        # 从外部接收参数
        data = {"mobile":mobile,"password":password}
        responses = requests.post(self.login_url,headers =self.headers,json = data)
        return  responses
import app
import requests


class EmpApi:
    def __init__(self):
        self.emp_url = app.HOST + '/api/sys/user'
        self.headers = app.HEADERS
        pass

    def add_emp(self, username, mobile):
        '''添加员工请求方法'''
        data = {
            "username": username,
            "mobile": mobile,
            "timeOfEntry": "2020-01-28",
            "formOfEmployment": 2,
            "workNumber": "12321214",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2020-01-20T16:00:00.000Z"
        }

        # 发送增加员工请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        # 返回请求添加员工请求的响应数据

        # print(response)
        return response

    def query_emp(self):
        '''查询员工请求方法'''
        url = self.emp_url + '/' + app.EMP_ID
        response = requests.get(url,headers=self.headers)
        return response
    def modify_emp(self,username,password): #这里只修改两个参数，实际创建时，需要全部参数参数化
        '''更改员工请求方法'''
        url = self.emp_url + '/' + app.EMP_ID
        response = requests.put(url,json={"username":username,"password":password},headers=self.headers)
        return response
    def remove_emp(self):
        '''删除员工请求方法'''
        #发送请求
        url = self.emp_url + '/' + app.EMP_ID
        return requests.delete(url,headers = self.headers)





if __name__ == '__main__':
    pass
    # EmpApi().add_emp('dan@#$','132231234224')

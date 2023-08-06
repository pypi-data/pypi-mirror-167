import json

import allure
import requests

from common.baserequest import BaseRequests
from common.baseresponse import BaseResponse
from tool.key_driver import KeyDriver


class SendRequest():
    dict_var={}

    def __init__(self,case):
        self.request=BaseRequests()
        self.request_data={}
        self.allure_data = {"feature": case["name"]}
        for key in case:
             if key in["before"]:
                 self.before=case["before"]
             elif key in["assert"]:
                self.assert_data=case["assert"]
             elif key in ["back"]:
                self.back=case["back"]
             elif key in ["story", "title"]:
                self.allure_data[key] = case[key]
             elif key in ["name","url","method","params","data","json","headers","files"]:
                 self.request_data[key]=case[key]
        for key in self.allure_data:
            getattr(allure.dynamic,key)(self.allure_data[key])




    def send(self):
        #第一步执行前置操作
        KeyDriver(self,self.before)
        #第二步发送请求
        self.request_data=json.loads(str(KeyDriver(self,self.request_data)))
        for key in self.request_data:
            setattr(self.request,key,self.request_data[key])


        resp=requests.request(
            method= self.request.method,
            url= self.request.url,
            params= self.request.params,
            data= self.request.data,
            json= self.request.json,
            headers= self.request.headers,
            files= self.request.files
        )
        self.response=BaseResponse(resp)
        # 第三部执行后置动作
        KeyDriver(self,self.back)

        KeyDriver(self,self.assert_data)
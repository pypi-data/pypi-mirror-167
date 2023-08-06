import json
import os

import requests

from tool.config import Config
from tool.tools import params_to_dict, headers_to_dict


class BaseConfig():
    __config=None
    @property
    def config(self):
        if self.__config is None:
            __class__.__config=Config()
        return self.__config

class Configdes(BaseConfig):
    def __set__(self, instance, value):
        pass
    def __get__(self, instance, owner):
        return self.config








class BaseRequests():
    method=None
    name=None
    __url=None
    __json=None
    __data=None
    __params=None
    __headers=None
    __files=None
    config=Configdes()


    @property   #把2一个方法定义成一个属性的装饰器
    def url(self):
        return self.config.get_ip(self.name) + self.__url
    @url.setter
    def url(self,value):
        self.__url=value


    @property
    def json(self):
        return self.__json
    @json.setter
    def json(self,value):
        try:
            self.__json=json.loads(value)
        except:
            self.__json=value




    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self,value):
        try:
            self.__data=json.loads(value)
        except:
            self.__data=value


    @property
    def params(self):
        return self.__params
    @params.setter
    def params(self,value):
        if isinstance(value,dict):
            self.__params=value
        elif isinstance(value,str):
            self.__params= params_to_dict(value)


    @property
    def headers(self):
        return self.__headers
    @headers.setter
    def headers(self,value):
        if not value:
            return
        try:
            self.__headers=json.loads(value)
        except:
            self.__headers=headers_to_dict(value)







    @property
    def files(self):
        if not self.__files:
            return
        try:
            self.__files = json.loads(self.__files)
        except:
            pass
        if isinstance(self.__files, dict):
            for i in self.__files:
                if isinstance(self.__files[i], str):
                    self.__files[i] = open(os.path.join(self.config.get_rootpath(), self.__files[i]), "rb")
        return self.__files

    @files.setter
    def files(self, value):
        self.__files = value


import configparser
import os

config=configparser.ConfigParser()
file_path=os.path.join(os.getcwd(),'config.ini')
config.read(file_path,encoding='utf-8')



class Config():
    def __init__(self):
        # 获取环境号
        # self.env=os.environ.get('env')
        self.env='test'

    def get_ip(self,name):
        section=f"{self.env}_ip"
        return self.get_option(section,name)




    def section_is_exist(self,section):
        return section in config.sections()


    def get_option(self,section,option):
        try:
            return config.get(section,option)
        except:
            assert False,'获取不到配置信息'

    def get_rootpath(self):
        root_path=self.get_option("root_path","path")
        if root_path =="":
            root_path=os.path.dirname(file_path)
        return root_path



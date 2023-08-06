import logging



#获取日志记录器
import os
from logging.handlers import TimedRotatingFileHandler

logger=logging.getLogger("自动化框架搭建")
logger.setLevel(level=logging.DEBUG)  # 设置日志记录器的最低级别
file_path=os.path.join(os.getcwd(),"logs/") #生成文件的位置
if not os.path.exists(file_path):  #判断文件是否存在，如果不存在就创建一个
    os.mkdir(file_path)

#debug日志
#创建文件hander
# 创建一个按大小自动切割日志的日志处理器。 root_path + 'api.log' api日志路径，maxBytes 设置日志切割大小，单位时byte
# backupCount 设置备份文件的最大个数，encoding 设置日志文件编码格式
hander=TimedRotatingFileHandler(file_path+"api.log",when="d",interval=1,backupCount=15,encoding="utf-8")
hander.setLevel(logging.DEBUG)
# 创建一个日志格式化器
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # 日志格式化期和日志处理器绑定
hander.setFormatter(formatter)
logger.addHandler(hander)


#报错日志
hander2=TimedRotatingFileHandler(file_path+"erro.log",when="d",interval=1,backupCount=15,encoding="utf-8")
hander2.setLevel(logging.ERROR)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
hander2.setFormatter(formatter)
logger.addHandler(hander2)


#正常处理日志
hander3=logging.StreamHandler()
hander3.setLevel(logging.DEBUG)
formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
hander3.setFormatter(formatter)
logger.addHandler(hander3)


def info(msg):
    logger.info(msg)

def erro(msg):
    logger.error(msg)

def debug(msg):
    logger.debug(msg)
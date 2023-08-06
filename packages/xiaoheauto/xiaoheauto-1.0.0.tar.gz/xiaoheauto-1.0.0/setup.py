from setuptools import setup, find_packages

setup(
    name='xiaoheauto',  # 包名    pip install 包名
    version='1.0.0',  # 版本
    keywords=["api","auto"],
    description="test packge auto",  # 包简介
    long_description='Interface automation framework',  # 读取文件中介绍包的详细内容
    author='hezhibin',  # 作者
    author_email='2587071020@qq.com',  # 作者邮件
    license='MIT License',  # 协议
    url='https://gitee.com/hestudyit/autoapi.git',  # github或者自己的网站地址
    packages=['tool','common'],    #发布的包列表
    platforms='python',
    install_requires=[
        'allure-pytest==2.10.0',
        'configparser==5.2.0',
        'jsonpath==0.82',
        'pytest==7.1.2',
        'requests==2.28.1',
        'xlrd==2.0.1',
    ]  # 安装所需要的库

)
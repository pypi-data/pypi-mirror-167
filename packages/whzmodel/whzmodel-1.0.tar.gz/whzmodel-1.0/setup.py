from setuptools import setup

setup(
    name='whzmodel',# 需要打包的名字,即本模块要发布的名字
    version='v1.0',#版本
    description='A  module for test', # 简要描述
    py_modules=['whzmodel'],   #  需要打包的模块
    author='whzikaros', # 作者名
    author_email='1345146183@qq.com',   # 作者邮件
    # requires=['requests','urllib3'], # 依赖包,如果没有,可以不要
    license='MIT'
)
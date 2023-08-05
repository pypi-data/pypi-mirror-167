from setuptools import setup

# README_rst = ''
# with open('README.rst', mode='r', encoding='utf-8') as fd:
#     README_rst = fd.read()

setup(
    name='TestNewBao',
    version='0.4', 
    author='吴儒林',
    author_email='946317637@qq.com',
    # url='项目首页，可以是github的url',
    description='包的概述',
    long_description='使用说明',
    packages=['TestNewBao'],
#     long_description=README_rst,
    include_package_data=True,#为了使用强制MANIFEST.in建立车轮和Win32安装时（否则MANIFEST.in将只能用于源码包/ ZIP）
    py_modules = ["TestNewBao.putText"],         # 要打包的模块，多个用逗号分开
    install_requires=['cython']
)

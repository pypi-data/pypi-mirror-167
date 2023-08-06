from setuptools import setup

# README_rst = ''
# with open('README.rst', mode='r', encoding='utf-8') as fd:
#     README_rst = fd.read()

setup(
    name='scratch3py_wurulin',
    version='0.1.0', 
    author='吴儒林',
    author_email='946317637@qq.com',
    # url='项目首页，可以是github的url',
    description='模拟Scratch，让python像Scarch一样的制作游戏和动画',
    long_description='模拟Scratch，让python像Scarch一样的制作游戏和动画',
    packages=['scratch3py_wurulin'],
#     long_description=README_rst,
    include_package_data=True,#为了使用强制MANIFEST.in建立车轮和Win32安装时（否则MANIFEST.in将只能用于源码包/ ZIP）
    py_modules = ["scratch3py_wurulin.sddd"],         # 要打包的模块，多个用逗号分开
    install_requires=['PIL','numpy']          # 预装依赖库
)

"""
包
一个包含多个模块的特殊目录
目录下有一个特殊的文件 __init__.py
包名的命名方式和变量名一致，小写字母 + '_'

Pycharm 建包的两种方式
1）新建目录 Directory, 在目录下新建 __init__.py 文件
2）右键直接选 Python Package

__init__.py     指定对外界提供的模块列表
from . import send_message
from . import receive_message  # . 当前目录     send_message  receive_message 模块名

发布模块
1）创建 setup.py
2）构建模块
$ python3 setup.py build
3）生成发布压缩包
$ python3 setup.py sdit

安装模块
tar -zxvf 压缩包
sudo python3 setup.py install

卸载模块 —— 直接从安装目录下把安装模块的目录删除即可

cd /usr/local/b/pythonx.x/dist-package/  # __file__
sudo rm -r ______包名

setup.py

from distutils.core import setup
setup(name = 'pel',  #
    version = '1.0',  #
    description = '描述信息',  #
    long_description = '完整描述信息',  #
    author = '作者',
    author_email = '作者邮箱',  #
    url = '主页',  #
    py_modules = ['模块名1','模块名2']  # 包名.模块名
)


setup(**kwargs)  # 有关字典参数的详细信息,可参阅官方网站
                 # docs.python.org/2/distutils/apiref.html

# 卸载模块 —— 直接从安装目录下把安装模块删除即可
# cd /usr/local/lib/pythonx.x/dist-packages/     -----  __file__
# sudo rm -r ____ ---->包名
"""
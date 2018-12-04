#在Python中，安装第三方模块，是通过包管理工具pip完成的。
# 如果你正在使用Mac或Linux，安装pip本身这个步骤就可以跳过了。
#
# 例如，我们要安装一个第三方库——Python Imaging Library，这是Python下非常强大的处理图像的工具库。不过，PIL目前只支持到Python 2.7，并且有年头没有更新了，因此，基于PIL的Pillow项目开发非常活跃，并且支持最新的Python 3。
#
# 一般来说，第三方库都会在Python官方的pypi.python.org网站注册，要安装一个第三方库，必须先知道该库的名称，可以在官网或者pypi上搜索，比如Pillow的名称叫Pillow，因此，安装Pillow的命令就是：
#
# pip install Pillow

# 在使用Python时，我们经常需要用到很多第三方库，例如，上面提到的Pillow，以及MySQL驱动程序，Web框架Flask，科学计算Numpy等。用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda，这是一个基于Python的数据处理和科学计算平台，它已经内置了许多非常有用的第三方库，我们装上Anaconda，就相当于把数十个第三方模块自动安装好了，非常简单易用。

# 模块搜索路径
# 当我们试图加载一个模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错：
# import mydodule  错误M oduleNotFoundError: No module named 'mydodule'
import  sys
print(sys.path)

# 如果我们要添加自己的搜索目录，有两种方法：
#
# 一是直接修改sys.path，添加要搜索的目录：

import sys
#添加一个自己创建的目录
sys.path.append('/Users/michael/my_py_scripts')
print(sys.path)
# 如果我们要操作文件、目录，可以在命令行下面输入操作系统提供的各种命令来完成。比如dir、cp等命令
# 要在Python程序中执行这些目录和文件的操作怎么办？其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，
# Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os
print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数：
print(os.uname())

# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)
print('-----------------\n\n\n')
# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

#查看当前目录的绝对路径
print(os.path.abspath('.'))
#/Users/poyan/Desktop/python/10

#查看上层目录的绝对路径
print(os.path.abspath('../'))
#/Users/poyan/Desktop/python

#在某个目录下创建一个新目录  ，首先把新目录的完整路径表示出来:
path = os.path.abspath('.')
newPath = os.path.join(path, '03dir')

#创建一个目录, 如果已经存在，则会报错
if not  os.path.isdir(path):
    os.mkdir(newPath)

# os.mkdir()创建路径中的最后一级目录，而如果之前的目录不存在并且也需要创建的话，就会报错。
#
# os.makedirs()创建多层目录，如果中间目录都不存在的话，会自动创建。

# os.mkdir(newPath)

#删掉一个目录 #如果不存在，则会报错
# os.rmdir(newPath)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，
# 这样可以正确处理不同操作系统的路径分隔符。在Linux/Unix/Mac下，os.path.join()返回这样的字符串：
# part-1/part-2
# 而Windows下会返回这样的字符串：
# part-1\part-2

# 要拆分路径时，也不要直接去拆字符串，而要通过s.path.split()函数，这样可以把一个路径拆分为两部分(从后边拆分，
# 后一部分总是最后级别的目录或文件名：
print(newPath)  #/Users/poyan/Desktop/python/10/03dir
print(os.path.split(newPath)) #('/Users/poyan/Desktop/python/10', '03dir')

print(os.path.split('/Users/michael/testdir/file.txt'))  #('/Users/michael/testdir', 'file.txt')

# 得到文件拓展名
print(os.path.splitext('/path/to/file.text'))   #('/path/to/file', '.text')


# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。

# 文件操作使用下面的函数。假定当前目录下有一个test.txt文件：
# 重命名文件
# os.rename('03test.text', '03test.py')

# 删掉文件:
#  os.remove('test.py')

#  shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#文件存在
filePath = os.path.join(os.getcwd(), '03.操作文件和目录.py')
print(os.path.isfile(filePath))

#文件夹存在
print(os.path.isdir(newPath))
print('-----------------------')
# 如果要检测路径是一个文件或目录可以使用 exists() 方法：
print(os.path.exists(newPath))
print(os.path.exists(filePath))

#获得当前工作目录
print(os.getcwd())  #/Users/poyan/Desktop/python/10
rootPath = os.getcwd()
# 返回指定目录下的所有文件和目录名(不会递归）
print(os.listdir(rootPath))

#判断是否是绝对路径
print(os.path.isabs(filePath))

#获取文件大小
print(os.path.getsize(filePath))  #3858


#查看当前目录下的文件夹
L = [x for x in os.listdir('.') if os.path.isdir(x)]
print(L )
#查看当前目录下的py文件
L = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(L )
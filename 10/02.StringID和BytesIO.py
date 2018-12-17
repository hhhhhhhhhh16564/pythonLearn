# StringIO
# 很多时候，数据读写不一定是文件，也可以在内存中读写。
#
# StringIO顾名思义就是在内存中读写str。

# 要把str写入StringIO，我们需要先创建一个StringIO，然后，像文件一样写入即可：

from io import StringIO
f = StringIO()
f.write('hello')  #返回值为字符串的长度
f.write(' ')
f.write('world!')
print(f.write('Michael'), f.getvalue())

#getValue()方法用于获得写入后的str
f = StringIO('Hello! \n Hi! \n Goodbye! \n 哈哈哈')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())
# Hello!
# Hi!
# Goodbye!
# 哈哈哈


# StringIO操作的只是str, 如果要操作二进制数据, 就需要使用BytesIO
from io import BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))
print(f.getvalue())
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。

# 和StringIO类似，可以用一个bytes初始化BytesIO，然后，像读文件一样读取：
from io import BytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read().decode('utf-8'))




from io import StringIO

f = StringIO()
f.write('Hello World')
f.seek(0)  #写完之后，偏移量为末尾, 要想读内容，则要放到首位
s = f.readline()
print(s)





















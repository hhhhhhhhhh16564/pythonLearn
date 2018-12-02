#生成[1x1, 2x2, 3x3, ..., 10x10]怎样做呢
#传统的方法是进行循环添加

print([x * x for x in range(1, 11)])

#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
print([x * x for x in range(1, 11) if x % 2 == 0])

#还可以使用两层循环，可以生成全排列：['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']
print([m + n for m in  'ABC' for n in  'XYZ'])

#python 字符串拼接用+

#用列表列出当前文件下的所有目录和文件名

import  os
print([d for d in os.listdir('.')])

# os.listdir('.')可以列出文件和目录
#for循环其实可以同时使用两个甚至多个变量，比如dict的items()可以同时迭代key和value：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
for k, v in d.items():
    print(k, '=', v)

#['x=A', 'y=B', 'z=C']
print([k + '=' + v for k, v in d.items()])


# 使用内建的isinstance函数可以判断一个变量是不是字符串：
print(isinstance('x', str))
L1 = ['Hello', 'World', 18, 'Apple', None]

#['hello', 'world', 'apple']
print([x.lower() for  x in  L1 if isinstance(x, str)])









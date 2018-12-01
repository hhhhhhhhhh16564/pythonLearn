L = [1, 2, 3, 4, 5, 6, 7, 8, 9]

#取前三个元素
print(L[0:3])

#L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

print(L[:3])
print(L[5:6])

#类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
print(L[-2:])
print(L[-2:-1])

L = list(range(100))
#前10个数
print(L[:10])

#后10个数
print(L[-10:])

#前11-20个数：
print(L[10:20])

#所有数，每两个取一个
print(L[::5])

#前10个数，每两个取一个
print(L[:10:2])

#tunple 也可以进行切片操作
#字符串'xxx'也可以看成是一种list，每个元素就是一个字符。因此，字符串也可以用切片操作，只是操作结果仍是字符串：

str = 'ABCDEFG'
print(str[:3])

print(str[::2])


#去电字符串首尾的空格
def trim(s):
    while len(s) > 0:
        if s[0] == ' ':
            s = s[1:]
        elif s[-1] == ' ':
            s = s[:-1]
        else:
            return s

print(trim('    jjjkkk ll ff'))










































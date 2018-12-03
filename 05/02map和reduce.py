#map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
L = list(range(1, 11))
print(L)

def f(x):
    return x * x

#map函数的返回值是Iterator 可以不断调用next
s = map(f, L)

#将Iterator转换为列表
print(list(s))

# [1, 2, 3, 4, 5, 6, 7, 8, 9] 将数组的整数转换为字符串
print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))

#再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)

#序列求和
from  functools import  reduce
def add(x, y):
    return x + y
print(reduce(add,[1,2,3,4,5]))

#将字符串转换为整数
digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2toInt(s):
    def chartTonumber(s):
        return digits[s]
    def fn(x, y):
        return 10 * x + y
    return reduce(fn, map(chartTonumber, s))

print(str2toInt('13579'))

#还可以用lambda函数进一步简化成：
def str2toInt(s):
    def chartTonumber(s):
        return digits[s]
    return reduce(lambda x, y : 10 * x + y, map(chartTonumber, s))

print(str2toInt('9876543'))


#练习1. 利用map()函数，把用户输入的不规范的英文名字，变为首字母大写，其他小写的规范名字。输入：['adam', 'LISA', 'barT']，输出：['Adam', 'Lisa', 'Bart']：

L = ['adam', 'LISA', 'barT']

def charSwitch(s):
    return s[0].upper() + s[1:].lower()

print(charSwitch('abD'))
print(list(map(charSwitch, L)))

#练习2 利用map和reduce编写一个str2float函数，把字符串'123.456'转换成浮点数123.456：

digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def str2toFloat(s):
    def chartTonumber(s):
        return digits[s]
    def fn(x, y):
        return 10 * x + y
    def indexpoint(L):
        L1 = L
        L2 = '0'
        for i in range(len(L)):
            if L[i] == '.':
                L1 = L[:i]
                L2 = L[i+1:]
                if i == 0:
                    L1 = '0'

        return (L1, L2)
    LL = indexpoint(s)
    L1 = LL[0]
    L2 = LL[1]

    return reduce(fn, map(chartTonumber, L1)) + reduce(fn, map(chartTonumber, L2)) * pow(10,-len(L2))

print(str2toFloat('10.19100'))









#默认参数
def power(x, n= 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(100))
print(power(100, 3))

# 一是必选参数在前，默认参数在后，否则Python的解释器会报错（思考一下为什么默认参数不能放在必选参数前面）；
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。

def enroll(name, gender, age = 6, city= 'beijing'):
    print('name', name)
    print('gender', gender)
    print('age', age)
    print('city', city)
enroll('张三', '男')

#也可以不按顺序提供部分默认参数。当不按顺序提供部分默认参数时，需要把参数名写上
enroll('lisi', 'women', city = 'shagnhai')


#默认参数很有用，但使用不当，也会掉坑里。默认参数有个最大的坑，演示如下
def add_end(L=[]):
    L.append('end')
    return L
#正确
print(add_end([1,3,5]))

#使用默认参数 连续调用两次错误
add_end()
add_end()

#正确结果打印1个 end 实际上打印 ['end', 'end', 'end']add_end()
print(add_end())

#Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
def add_end(L= None):
    if L is None:
        L = []
    L.append('end')
    return L
add_end()
add_end()
add_end()
print(add_end())


#可变参数
#在Python函数中，还可以定义可变参数。顾名思义，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。
#我们以数学题为例子，给定一组数字a，b，c……，请计算a2 + b2 + c2 + ……。

# 参数1组装为list 或者tuple
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc([1, 3, 5]))

# 参数变为可变参数
#定义可变参数和定义一个list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1, 3, 5))
print(calc())

#如果已经有一个list或者tuple，要调用一个可变参数怎么办？可以这样做：
numbs = [1, 2, 3]
print(calc(numbs[0], numbs[1], numbs[2]))
#*nums表示把nums这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见。
print(calc(*numbs))


#关键字参数
#可变参数内部组装为tuple  关键字参数组装为dict
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other', kw)

person('michael', 30)
#可以传入任意个数的关键字参数:
person('michael', 65, city='beijing', gender='M')

#和可变参数类似，也可以先组装出一个dict，然后，把该dict转换为关键字参数传进去：extra = {'city': 'Beijing', 'job': 'Engineer'}
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('zhangsan', 24, city=extra['city'], job=extra['job'])

#类似可变参数 可以，调用时加上**直接传递dict
person('zhangsan', 24, **extra)

#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)

person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


#命名关键字参数（要限制关键字参数的名字，）
#果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)

#和关键字参数**kw不同，命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数。
person('jack', 28, city='beijing', job='teacher')



#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person(name, age, *args, city, job):
    print(name, age, args, city, job)

#命名关键字参数必须传入参数名，这和位置参数不同。如果没有传入参数名，调用将报错：
#命名关键字参数，可以有缺省值，类似默认参数，从而简化调用：
def person(name, age, *, city='beijing', job):
    print(name, age, city, job)
person('jack', 2567, job='teacher')

#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person(name, age, city, job):
    # 缺少 *，city和job被视为位置参数
    pass

#参数组合

#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。

def f1(a, b, c=-100, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=-200, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1,2)
f1(1, 2, c=3)
f1(1, 2, 3, 'm', 'n', 'x', 'y')
f2(1, 2, 3, d=99, extra=888)

#最神奇的是通过一个tuple和dict，你也可以调用上述函数：
args = (11, 22, 33, 44)
kw = {'d': -100, 'x':-200}
f1(*args, **kw)

args = (11, 22, 33)
f2(*args, **kw)



#要注意定义可变参数和关键字参数的语法：

# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。
#
# 命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。
#
# 定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。






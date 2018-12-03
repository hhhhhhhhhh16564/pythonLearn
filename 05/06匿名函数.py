#当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。

L = list(map(lambda x : x * x, list(range(1, 100))))
print(L)

#通过对比可以看出，匿名函数lambda x: x * x实际上就是：
# def f(x):
#     return x * x
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。

# 匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。

#用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：

f = lambda  x : x * x
print(f(111111))

#同样，也可以把匿名函数作为返回值返回，比如：

#匿名函数：后边是表达式的值 ： 前边可以不写参数，后边直接用

def build(x, y):
    return lambda : x * x + y * y

print(build(3, 4)())

L = list(filter(lambda x : x % 2 == 1, range(1, 20)))
print(L)
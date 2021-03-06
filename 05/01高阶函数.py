#函数本身也可以赋值给变量，即：变量可以指向函数。

#如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：
f = abs
print(f(10))

#那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
#如果函数指向其他的对象，再次调用会报错
# abs = 5;
# abs(6) 会报错

#注：由于abs函数实际上是定义在import builtins模块中的，所以要让修改abs变量的指向在其它模块也生效，要用import builtins; builtins.abs = 10。

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x, y, f):
    return  f(x) + f(y)
print(add(-5, 6, abs))








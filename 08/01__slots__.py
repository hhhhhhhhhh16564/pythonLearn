class Student(object):
    pass

s = Student()
s.name = 'Michael'         # 动态给实例绑定一个属性
print(s.name)

# 还可以尝试给实例绑定一个方法：

def set_age(self, age):
    self.age = age

from types import MethodType
s.set_age = MethodType(set_age, s)              #给实例绑定一个方法
s.set_age(25)
print(s.age)

#但是给一个实例绑定的方法，对另一个实例是不起作用的
#为了给所有的实例都绑定方法，可以给class绑定方法

def set_score(self, score):
    self.score = score

Student.set_score = set_score

#给class绑定方法后, 所有的实例均可调用

s1 = Student()
s.set_score(111)
s1.set_score(999)

print(s.score , s1.score)

#通常情况下，上面的set_score方法可以直接定义在class中，但动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。

# 使用__slots__
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。
#
# Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：

class Student(object):
    __slots__ = ('name', 'age')

s = Student()
s.name = 'Michael'
s.age = 888
# s.score = 99  会报错
print(s.name, s.age)

# 由于'score'没有被放到__slots__中，所以不能绑定score属性，试图绑定score将得到AttributeError的错误。
#使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。


#使用__slots__后，类属性里就没有默认的__dict__了。














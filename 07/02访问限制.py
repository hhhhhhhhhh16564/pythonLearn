# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
#
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:  %s' % (self.name, self.score))
s = Student('hhh', 98)
s.print_score()
#也可以改变类型
s.name = 100
s.score = 88
s.print_score()

print('**********************************************************')
# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s:  %s' % (self.__name, self.__score))
    def get_name(self):
        return self.__name
    def get_score(self):
        return self.__score
    def set_name(self,name):
        self.__name = name
    def set_score(self, score):
        self.__score = score



s = Student('hhh', 98)
s.print_score()
#也可以改变类型
s.name = 100
s.score = 88
# s.print_score()  结果hhh:  98(因为上边两行实际上是新增添了两个属性
# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：
# 如果又要允许外部代码修改score怎么办？可以再给Student类增加set_score方法：
# 你也许会问，原先那种直接通过bart.score = 99也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数：
# def set_score(self, score):
#     if 0 <= score <= 100:
#         self.__score = score
#     else:
#         raise ValueError('bad score')

# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。

# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。


# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，所以，仍然可以通过_Student__name来访问__name变量：

print(s.get_name())
print(s._Student__name)

#但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
s.__name = 'aaaaaaa'

print(s.get_name())  #仍打印hhh
print(s.__name)      #打印aaaaaaa

#原因 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：



#判断一个变量是否在一个序列内

if 'tt' in ['tt', 'hh']:
    print('包含')
else:
    print('不包含')

s1 =  Student('hhh', 98)
s2 =  Student('hhh', 98)
s3 =  Student('hhh', 98)

if s1 in [s1, s2]:
    print('包含对象')
else:
    print('不包含对象')


























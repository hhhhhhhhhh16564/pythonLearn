# 仍以Student类为例，在Python中，定义类是通过class关键字
class Student(object):
    pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
bart = Student()
print(bart)

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name = '小明'
print(bart.name)

# 由于类可以起到模板的作用，因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
 # 注意：特殊方法“__init__”前后分别有两个下划线！！！

# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
#
# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：

s = Student('xiaomig', 25)
print(s.name, s.score)

# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数、关键字参数和命名关键字参数。

#数据封装
#s = Student('xiaomig', 25) 在上面的Student类中，每个实例就拥有各自的name和score这些数据。我们可以通过函数来访问这些数据，
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:  %s' % (self.name, self.score))


s = Student('hhh', 255)
s.print_score()
# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：
# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
#
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
#
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同







# 仍以Student类为例，在Python中，定义类是通过class关键字
class Student(object):
    pass
# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
bart = Student()
print(bart)

# 可以自由地给一个实例变量绑定属性，比如，给实例bart绑定一个name属性：
bart.name = '小明'
print(bart.name)




















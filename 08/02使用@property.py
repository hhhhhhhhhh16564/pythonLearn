#在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：

# 可以通过一个set_score()方法来设置成绩，再通过一个get_score()来获取成绩， 但是，调用方法又略显复杂，没有直接用属性这么直接简单。
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。Python内置的@property装饰器就是负责把一个方法变成属性调用的：

class Student(object):
    @property
    def score(self):
        return  self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 - 100!')
        self._score = value
# @property的实现比较复杂，我们先考察如何使用。把一个getter方法变成属性，只需要加上@property就可以了，此时，@property本身又创建了另一个装饰器@score.setter，负责把一个setter方法变成属性赋值，于是，我们就拥有一个可控的属性操作：

s = Student()
s.score = 60      # OK，实际转化为s.set_score(60)
print(s.score)   #OK，实际转化为s.get_score()
# print(s._score)     #内部变量是_score,所以可以访问  如果是__score，则是私有变量,需要通过_Student__score访问


# 注意到这个神奇的@property，我们在对实例属性操作的时候，就知道该属性很可能不是直接暴露的，而是通过getter和setter方法来实现的。

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：

class Student(object):
    @property
    def birth(self):
        return self._birth
    @birth.setter
    def birth(self, value):
        self._birth = value

    def age(self):
        return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。


# 请利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution：

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, width):
        self._width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        self._height = height

    @property
    def resolution(self):
        return self._width * self._height

s = Screen()
s.width = 100
s.height = 12
print(s.width, s.height, s.resolution)








































































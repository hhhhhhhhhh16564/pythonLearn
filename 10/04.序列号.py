# 我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling，
# 在其他语言中也被称之为serialization，marshalling，flattening等等，都是一个意思。
# 序列化之后，就可以把序列化后的内容写入磁盘，或者通过网络传输到别的机器上。
# 反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling。
# Python提供了pickle模块来实现序列化。

import pickle

#序列化
d = {"name": '小明', "age":87, "grade":"二年级"}
content = pickle.dumps(d)
print(content)
# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。
# 或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

f = open('04.dump.txt', 'wb')
pickle.dump(d, f)
f.close()

# 当我们要把对象从磁盘读到内存时，可以先把内容读到一个bytes，然后用pickle.loads()方法反序列化出对象，
# 也可以直接用pickle.load()方法从一个file-like Object中直接反序列化出对象。
# 我们打开另一个Python命令行来反序列化刚才保存的对象：
f = open('04.dump.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)
print('--------------------------------------')
# JSON类型	Python类型
# {}	     dict
# []	     list
# "string"	str
# 1234.56	int或float
# true/false	True/False
# null	None
# Python内置的json模块提供了非常完善的Python对象到JSON格式的转换。我们先看看如何把Python对象变成一个JSON：
import json
d = {"name": 'xiaoming', "age":87, "grade":"two"}
print(d)
print(json.dumps(d))
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))
# 由于JSON标准规定JSON编码是UTF-8，所以我们总是能正确地在Python的str与JSON的字符串之间转换。

class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score
    def __str__(self):
        return 'Student:objec %s %s %s' % (self.name, self.age, self.score)

s = Student('Bob', 20, 80)

# json.dumps可选参数default就是把任意一个对象变成一个可序列为JSON的对象，我们只需要为Student专门写一个转换函数，再把函数传进去即可：
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

print(json.dumps(s, default=student2dict))


# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。


print(r'\\\\\\\\\\\\\\\\\\\\\\\\\\')
print(json.dumps(s, default=lambda obj:obj.__dict__))


# 同样的道理，如果我们要把JSON反序 列化为一个Student对象实例，
# loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：

def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


#
# Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。
# json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。
# 但是，当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
# 既做到了接口简单易用，又做到了充分的扩展性和灵活性。


#可以将自定义的对象直接转化为json存入文件中
s = Student('Bob', 2000, 8000)
f = open('041.dump.txt', 'wb')
pickle.dump(s, f)
f.close()


f = open('041.dump.txt', 'rb')
content = pickle.load(f)
f.close()

print(content, '-------------')


#排序算法
L = [2, 3, 8, 1, -8, 5]
print([sorted(L)])

#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序，例如按绝对值大小排序：
print(sorted(L, key=abs))

#字符串排序，默认是ascii比较
names = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(names))

#忽略大小写
#要传一个方法的类
print(sorted(names, key=str.lower))

#要是进行反向排序的话，传入第三个参数 reverse
print(sorted(names, key=str.lower, reverse=True))


#假设我们用一组tuple表示学生名字和成绩：
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按照名字排序
print(sorted(L, key=lambda x: x[0]))
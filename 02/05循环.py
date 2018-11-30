sum = 0
for x in [1, 2, 3, 4, 5]:
    sum = sum + x
print(sum)

#range(5)生成的序列是从0开始小于5的整数
# 0 1 2 3 4

print(list(range(5)))

# 计算1到100的合
sum = 0
for x in list(range(101)):
    sum = sum + x
print(sum)

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)


n = 1
while n <= 100:
    if n > 10:
        break
    print(n)
    n = n + 1
print('END')
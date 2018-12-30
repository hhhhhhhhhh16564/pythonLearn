# 字符串编码一直是令人非常头疼的问题，尤其是我们在处理一些不规范的第三方网页的时候。虽然Python提供了Unicode表示的str和bytes两种数据类型，
# 并且可以通过encode()和decode()方法转换，但是，在不知道编码的情况下，对bytes做decode()不好做。

# 对于未知编码的bytes，要把它转换成str，需要先“猜测”编码。猜测的方式是先收集各种编码的特征字符，根据特征字符判断，就能有很大概率“猜对”。
# 当然，我们肯定不能从头自己写这个检测编码的功能，这样做费时费力。chardet这个第三方库正好就派上了用场。用它来检测编码，简单易用。

import chardet

r = chardet.detect(b'Hello, world')
print(r)
# {'encoding': 'ascii', 'confidence': 1.0, 'language': ''}

# 检测出的编码是ascii，注意到还有个confidence字段，表示检测的概率是1.0（即100%）。

data = '离离原上草，一岁一枯荣'.encode('gbk')
r = chardet.detect(data)

print(r)

# 我们再试试对日文进行检测：
data = '最新の主要ニュース'.encode('euc-jp')
r = chardet.detect(data)
print(r)

f = open('/Users/poyan/Downloads/1111.txt', 'rb')
data = f.read()
print(chardet.detect(data))
print(data.decode('utf-8'))

# 不知道为啥
# UnicodeDecodeError: 'utf-8' codec can't decode byte 0xb1 in position 0: invalid start byte
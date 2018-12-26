# Python没有专门处理字节的数据类型。但由于b'str'可以表示字节，所以，字节数组＝二进制str。而在C语言中，
# 我们可以很方便地用struct、union来处理字节，以及字节和int，float的转换。
# 在Python中，比方说要把一个32位无符号整数变成字节，也就是4个长度的bytes，你得配合位运算符这么写：
n = 10240099
b1 = (n & 0xff000000) >> 24
b2 = (n & 0xff0000) >> 16
b3 = (n & 0xff00) >> 8
b4 = n & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)
print(b1, b2, b3, b4)


# 非常麻烦。如果换成浮点数就无能为力了。
# 好在Python提供了一个struct模块来解决bytes和其他二进制数据类型的转换。
# struct的pack函数把任意数据类型变成bytes：
import struct
b = struct.pack('>I', 10240099)
print(b)

# pack的第一个参数是处理指令，'>I'的意思是：
#
# >表示字节顺序是big-endian，也就是网络序，I表示4字节无符号整数。
#
# 后面的参数个数要和处理指令一致。

#unpack把bytes 变成相应的数据类型
t = struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80')

print(t)

# 根据>IH的说明，后面的bytes依次变为I：4字节无符号整数和H：2字节无符号整数。
# Windows的位图文件（.bmp）是一种非常简单的文件格式，我们来用struct分析一下。

# 首先找一个bmp文件，没有的话用“画图”画一个。

s = b'\x42\x4d\x38\x8c\x0a\x00\x00\x00\x00\x00\x36\x00\x00\x00\x28\x00\x00\x00\x80\x02\x00\x00\x68\x01\x00\x00\x01\x00\x18\x00'

# MP格式采用小端方式存储数据，文件头的结构按顺序如下：
#
# 两个字节：'BM'表示Windows位图，'BA'表示OS/2位图；
# 一个4字节整数：表示位图大小；
# 一个4字节整数：保留位，始终为0；
# 一个4字节整数：实际图像的偏移量；
# 一个4字节整数：Header的字节数；
# 一个4字节整数：图像宽度；
# 一个4字节整数：图像高度；
# 一个2字节整数：始终为1；
# 一个2字节整数：颜色数。
print(struct.unpack('<ccIIIIIIHH', s))

# (b'B', b'M', 691256, 0, 54, 40, 640, 360, 1, 24)
#
def bmp_info(data):
    bmp_struct = struct.unpack('<ccccIIIIIIHH', data)
    if bmp_struct[0] == b'B' and bmp_struct[1] in (b'M', b'A'):
        return {
            'width':bmp_struct[6],
            'height':bmp_struct[7],
            'color':bmp_struct[9]
        }





# 操作图像
from PIL import Image
# 打开一个jpg图像文件，注意是当前路径:
im = Image.open('01.jpg')

#获得图像尺寸
w, h = im.size

#缩放到50%
# //指取整除  /带小数
im.thumbnail((w//2, h//2))
print('Resize image to: %sx%s' % (w//2, h//2))

# 把缩放后的图像用jpeg格式保存:
im.save('01thumbnail.jpg', 'jpeg')

# 其他功能如切片、旋转、滤镜、输出文字、调色板等一应俱全。
# 比如，模糊效果也只需几行代码
from PIL import  Image, ImageFilter

im = Image.open('011.jpg')
#应用模糊滤镜
im2 = im.filter(ImageFilter.BLUR)
im2.save('011blur.jpg', 'jpeg')


# PIL的ImageDraw提供了一系列绘图方法，让我们可以直接绘图。比如要生成字母验证码图片：

from PIL import Image, ImageFilter, ImageDraw, ImageFont
import random

#随机字母
def rndChar():
    return chr(random.randint(65, 90))
# 随机颜色1:
def rndColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))
#随机颜色2
def rndColor2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255,255,255))

#创建Font对象
font = ImageFont.truetype('Arial.ttf', 36)

#创建Draw对象
draw = ImageDraw.Draw(image)

#填充每个像素(像素如果不填充，默认是白色）
for x in  range(width):
    for y in  range(height):
        draw.point((x, y), fill=rndColor())

for t in  range(4):
    draw.text((60*t + 10, 10), rndChar(), font = font, fill=rndColor2())

#模糊
image = image.filter(ImageFilter.BLUR)
image.save('012code.jpg', 'jpeg')












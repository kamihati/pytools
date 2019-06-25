from PIL import Image, ImageDraw, ImageEnhance
from PIL import ImageChops, ImageFilter


# 打开指定路径的图片初始化一个PIL图像对象
pil_im = Image.open('test.png')

# 创建一个新的图像对象
# 红色背景,640*480的RGB空白图像
new_image = Image.new('RGB', (640, 480), (255, 0, 0))
new_image.save('2_1.png')

# 把图像转为灰度模式
pil_im_2 = pil_im.convert("L")
pil_im_2.save("2_2.png")

# 复制图像。返回给定图像的副本
im_dup = ImageChops.duplicate(pil_im)
# 返回结果应为RGB,三通道的图。灰度图则只有一个通道
print(im_dup.mode)
# 返回两幅图像之间像素差的绝对值形成的图像,两图完全一致。所以绝对值为0，则生成的图像为纯黑图片
im_diff = ImageChops.difference(pil_im, im_dup)
# im_diff.show()

draw = ImageDraw.Draw(pil_im)
# 从左上角到右下角画了一条线
draw.line((0, 0) + pil_im.size, fill=128)
print((0, 0) + pil_im.size)
# 从右上角到左下角画了一条线
draw.line((0, pil_im.size[1], pil_im.size[0], 0), fill=128)
print((0, pil_im.size[1], pil_im.size[0], 0))

# fill参数为填充色
# pil_im.show()


# 把原图的亮度降为一半显示
enhancer = ImageEnhance.Brightness(pil_im)
im0 = enhancer.enhance(0.5)
# im0.show()


im = Image.open("test.png")
im.show()
# 对图片进行滤波处理。若图片无噪点则处理前后无变化
imout = im.filter(ImageFilter.BLUR)
imout.show()

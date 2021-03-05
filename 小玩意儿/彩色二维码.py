#__author:jiche
#date: 2020/11/30
from MyQR import myqr
import os

version, level, qr_name = myqr.run(
  words="https://www.runoob.com/python3/python3-tutorial.html",     # 可以是字符串，也可以是网址(前面要加http(s)://)
  version=1,               # 设置容错率为最高
  level='H',               # f    控制纠错水平，范围是L、M、Q、H，从左到右依次升高
  picture="1.jpg",              # 将二维码和图片合成
  colorized=True,             # 彩色二维码
  contrast=1.0,              #用以调节图片的对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
  brightness=1.0,             #用来调节图片的亮度，其余用法和取值同上
  save_name="555.gif",           # 保存文件的名字，格式可以是jpg,png,bmp,gif
  save_dir=os.getcwd()          #控制位置
)
'''https://www.jb51.net/article/162448.htm'''
'''
words  二维码指向链接  str 输入链接或者句子作为参数
version 边长  int 控制边长 范围1-40 数字越大边长越大
level  纠错等级 str 控制纠错水平 范围是 L M Q H, 从左到右依次升高，默认H
picture  结合图片  str 将QR二维码图像与一张同目录下的图片相结合 产生一张黑白图片
colorized  颜色  bool  使产生的图片由黑白变为彩色的
contrast  对比度  float  调节图片的对比度 1.0表示原始图片 更小的值表示更低对比度  更大反之 默认1.0
brightness  亮度 float  调节图片的亮度 其余同上
save_name  输出文件名  str  默认输出文件名是 “qrcode.png”
save_dir  存储位置    str  默认存储位置是当前目录
'''
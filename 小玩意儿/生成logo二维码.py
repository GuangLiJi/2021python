#__author:jiche
#date: 2020/11/30
import qrcode
from PIL import Image
import os,sys

#参数 string:二维码字符串;path:生成的二维码保存路径;logo:logo文件路径
def gen_qrcode(string,path,logo=""):
    qr = qrcode.QRCode(
        version=2,      #控制二维码的大小：(25*25)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  #ERROR_CORRECT_H:30%的字码可被容错
        box_size=8,     #控制二维码中每个小格子包含的像素数
        border=1        #控制边框(二维码与图片边界的距离)包含的格子数(默认为4)
    )
    qr.add_data(string)
    qr.make(fit=True)
    img = qr.make_image()
    img = img.convert("RGBA")
    if logo and os.path.exists(logo):
        try:
            icon = Image.open(logo)
            img_w, img_h = img.size
        except Exception as e:
            print(e)
            sys.exit(1)
        factor = 4
        size_w = int(img_w / factor)
        size_h = int(img_h / factor)

        icon_w, icon_h = icon.size
        if icon_w > size_w:
            icon_w = size_w
        if icon_h > size_h:
            icon_h = size_h
        icon = icon.resize((icon_w,icon_h),Image.ANTIALIAS)

        w = int((img_w - icon_w) / 2)
        h = int((img_h - icon_h) / 2)
        icon = icon.convert("RGBA")
        img.paste(icon,(w,h),icon)
    img.save(path)
    #调用系统命令打开图片
    # xdg-open :在用户的首选应用程序中打开文件或url
    os.system('xdg-open %s' % path)

if __name__ == "__main__":
    info = "https://blog.csdn.net/suoyue_py"        #生成二维码的网址
    pic_path = "qrsuoyue.png"           #生成二维码保存的图片名
    logo_path = "1.jpg"              #生成二维码所用的图标
    gen_qrcode(info,pic_path,logo_path)     #调用函数
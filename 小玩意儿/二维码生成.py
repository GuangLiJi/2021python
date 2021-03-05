#__author:jiche
#date: 2020/11/30
# coding: utf-8
"""
filename: qrcode.py
Created by Tacey Wong at 16-9-22 下午10:34
"""
import qrcode
qr = qrcode.QRCode(
    version=10,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data('删')
qr.make(fit=True)
img = qr.make_image()
img.save('12.png')
'''
version：值为1~40的整数，控制二维码的大小（最小值是1，是个12×12的矩阵）。 如果想让程序自动确定，将值设置为 None 并使用 fit 参数即可。
error_correction：控制二维码的错误纠正功能。可取值下列4个常量。
　　ERROR_CORRECT_L：大约7%或更少的错误能被纠正。
　　ERROR_CORRECT_M（默认）：大约15%或更少的错误能被纠正。
　　ERROR_CORRECT_M：大约30%或更少的错误能被纠正。
box_size：控制二维码中每个小格子包含的像素数。
border：控制边框（二维码与图片边界的距离）包含的格子数（默认为4，是相关标准规定的最小值）
'''
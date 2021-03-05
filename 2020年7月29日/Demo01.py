import xlwt
import os

file_dir = "E:\工作日常\\2020-07"
workbook=xlwt.Workbook()
sheet0=workbook.add_sheet('sheet0')
n=0
for i in os.listdir(file_dir):
    sheet0.write(n,0,i)
    n+=1
workbook.save(r'C:\Users\jiche\Desktop\测试1.xlsx')

import os
import xlrd
#遍历文件夹
def walkFile (file):
    for root,dirs,files in os.walk(file):
#        root 表示当前正在访问的文件夹路径
        # dirs 表示该文件夹下额子目录名 list
        #files 表示改文件下的文件 list
        #遍历文件
        for f in files :

            print(os.path.join(f))  #遍历目录下所有的文件

def main():
    walkFile("E:\工作日常\物流事业部项目\物资流向管控")

if __name__=='__main__':
    main()
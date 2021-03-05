#__author:jiche
#date: 2020/12/1
fp= open('d:/test.txt','w')
print('奋斗成就更好的你',file=fp)
fp.close()
'''第二种方式，使用文件读写操作'''
with open('d:/test1.txt','w') as file:
    file.write("奋斗成就更好的你----")


print('----------------------------------')
#输出北京的天气预报
print()
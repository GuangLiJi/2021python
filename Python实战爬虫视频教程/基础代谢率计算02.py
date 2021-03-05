
y_or_no= input('是否选择退出？（y/n）:')
while y_or_no !='y':

   print('请输入一下数据，用空格分隔')
   info = input('性别 体重（kg） 身高（cm） 年龄：')
   cut_info=info.split(' ')

   try:
       gender = cut_info[0]
       weight = float(cut_info[1])
       height = float(cut_info[2])
       age = int(cut_info[3])
       #计算BMR值
       if gender == '男':
           BMR = 13.7*weight+5.0*height-6.8*age+66
       elif gender == '女':
           BMR = 9.7 * weight + 1.8 * height - 4.7 * age + 665
       else:
           BMR = -1
        #s输出结果
       if BMR == -1 :
           print('输入的性别有误')
       else:
           print('您的性别:{},体重:{}kg,身高:{}cm,年龄：{}'.format(gender,weight,height,age))
           print('您的BMR值是:{}大卡'.format(BMR))
   except ValueError :
      print('请输入正确的信息！')
   except ImportError :
      print('输入的信息过少')
   except :
       print('程序异常')
   y_or_no= input('是否选择退出？（y/n）:')
print('欢迎下次使用')
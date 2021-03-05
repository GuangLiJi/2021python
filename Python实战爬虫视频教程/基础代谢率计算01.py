
y_or_no= input('是否选择退出？（y/n）:')
while y_or_no !='y':

  gender = input('请输入性别（男/女）:')
  weight = float(input('请输入体重（kg）:'))
  height = float(input('请输入身高（cm）:'))
  age = int(input('请输入年龄：'))
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
    print('您的BMR值是:',BMR)
  y_or_no= input('是否选择退出？（y/n）:')
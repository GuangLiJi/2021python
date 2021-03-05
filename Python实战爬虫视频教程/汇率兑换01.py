#汇率
usd_vs_rmd = 6.70

#带单位的货币输入
currency_str_value = input('请输入带单位的货币金额：')
#获取货币单位
unit = currency_str_value[-3:]

print(unit)
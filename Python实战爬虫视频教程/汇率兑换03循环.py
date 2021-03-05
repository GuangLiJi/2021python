#汇率
usd_vs_rmb = 6.70
#带单位的货币输入
currency_str_value = input("请输入带单位的货币金额:")
while currency_str_value !='Q':
    # 获取货币单位
    unit = currency_str_value[-3:]
    if unit == 'CNY':
        # 输入的是人民币
        rmb_str_value = currency_str_value[:-3]
        # 将字符串转为数字
        rmb_value = eval(rmb_str_value)
        # 汇率计算
        usd_value = rmb_value / usd_vs_rmb
        # 输出结果
        print('美元（USD）金额是：', usd_value)

    elif unit == 'USD':
        # 输入的美元
        usd_str_value = currency_str_value[:-3]
        # 将字符串转为数字
        rmb_value = eval(usd_str_value)
        # 汇率计算
        rmb_value = rmb_value * usd_vs_rmb
        # 输出结果
        print('人民币（CNY）金额是：', rmb_value)

    else:
        print('对不起，目前只支持人民币（CNY）和美元（USD）的查询')
    currency_str_value = input("请输入带单位的货币金额:")
print('已退出，欢迎下次使用！')
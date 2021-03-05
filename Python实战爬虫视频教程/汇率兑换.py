rmb_srt_value = input('请输入人民币（CNY）金额：')
rmb_value = eval(rmb_srt_value)
usd_vs_rmb = 6.70
usd_value = rmb_value / usd_vs_rmb
print('美元（USD）金额是：',usd_value)

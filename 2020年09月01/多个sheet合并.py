import  xlrd
import  pandas as pd
from pandas import DataFrame
from openpyxl import load_workbook

excel_name = 'E:\工作日常\每日异常\\九月.xlsx' #表格地址＋表格名称
wb = xlrd.open_workbook(excel_name)
#获取workbook中所有的表格
sheets =wb.sheet_names()

#循环遍历所有的sheet
alldata = DataFrame()
for i in range(len(sheets)):
    df = pd.read_excel(excel_name,sheet_name=i,index_col=0,header=None)
    alldata = alldata.append(df)

#保存为新的sheet 首先新建sheet 合并后的数据保存到新的sheet中
writer = pd.ExcelWriter('E:\工作日常\每日异常\\1234.xlsx',engine='openpyxl')
book = load_workbook(writer.path)
writer.book = book

#利用dataframe.to_excle保存合并后的数据到新的sheet
alldata.to_excel(excel_writer=writer,sheet_name='ALLDATA',header=0)#生成新的sheet命名为ALLDATA
writer.save()
writer.close()
print('处理完成')
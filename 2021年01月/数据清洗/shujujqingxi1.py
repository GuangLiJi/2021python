import pandas as pd
import numpy
fileNameStr = 'E:\Download\朝阳医院2018年销售数据.xlsx'  #读取Ecxcel 数据
xls = pd.ExcelFile(fileNameStr,dtype='object')
salesDf = xls.parse('Sheet1',dtype='object')
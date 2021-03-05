import xlrd
from xlrd import xldate_as_tuple
import datetime
#导入需要读取的第一个Excel表格的路径
data1 = xlrd.open_workbook(r'E:\工作日常\2020-07\2020-07-01\物流事业部海螺流向管控项目维护跟踪表-2020-07-01.xlsx')
table = data1.sheets()[0]
#创建一个空列表，存储Excel的数据
tables = []
#将excel表格内容导入到tables列表中
def import_excel(excel):
  for rown in range(excel.nrows):
   array = {'road_name':'','bus_plate':'','timeline':'','road_type':'','site':''}
   array['road_name'] = table.cell_value(rown,0)
   array['bus_plate'] = table.cell_value(rown,1)
   if table.cell(rown,2).ctype == 3:
     date = xldate_as_tuple(table.cell(rown,2).value,0)
     array['timeline'] = datetime.datetime(*date)
   array['road_type'] = table.cell_value(rown,3)
   array['site'] = table.cell_value(rown,4)
   tables.append(array)
if __name__ == '__main__':
  #将excel表格的内容导入到列表中
  import_excel(table)
  for i in tables:
    print(i)
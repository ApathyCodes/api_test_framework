"""
提供解析Excel 数据功能  使用openpyxl.load_Workbook

"""

import os
from openpyxl import load_workbook
from openpyxl.workbook.workbook import Worksheet


BaseDir = os.path.dirname(os.path.dirname(__file__))
dataDir = os.path.join(BaseDir, 'data')

# data_test.xlsx 文件路径
excel_file = os.path.join(dataDir, "data_test.xlsx")
# 加载Excel文件
workbook = load_workbook(filename=excel_file)

# 获取sheet1 表单
worksheet:Worksheet = workbook.get_sheet_by_name('Sheet1')
print(workbook.sheetnames)

"""
# 读取Excel中sheet1
sheet1 = workbook['Sheet1']

"""

# 获取sheet 工作中行和列
print('列：', worksheet.columns, worksheet.max_column)
print('行', worksheet.rows, worksheet.max_row)


# print(Sheet1['A2'].value)
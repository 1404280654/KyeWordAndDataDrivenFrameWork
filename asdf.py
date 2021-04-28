#!/usr/bin/python3
import openpyxl
wb=openpyxl.load_workbook('ttt.xlsx')  #打开excel文件
print(wb.get_sheet_names())  #获取工作簿所有工作表名

a=wb.get_sheet_names()
sheet=wb.get_sheet_by_name(a[0])  #获取工作表
print(sheet.title)

sheet02=wb.get_active_sheet()  #获取活动的工作表
print(sheet02.title)

print("---------------")
print(sheet.iter_cols())
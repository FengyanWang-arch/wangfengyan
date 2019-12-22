#coding=utf-8
import xlrd

data=xlrd.open_workbook(r"D:\表3.应急物资储备库采集表.xls")

#table=data.sheets()[0]
#table=data.sheet_by_index(0)
table=data.sheet_by_name("储备库(请填写)")

nrows=table.nrows
ncols=table.ncols

print(nrows)
print(ncols)
print(table.row_values(0))
print(table.col_values(0))
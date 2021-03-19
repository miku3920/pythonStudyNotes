# pip install xlrd==1.2.0
import xlrd
import xlwt


path = __file__
path = path[:path.rfind('\\')][:path.rfind('/')]+"\\"

read=xlrd.open_workbook(path+'發票.xlsx')
sheet=read.sheets()[0]
print(sheet.nrows)
print(sheet.ncols)

for i in range(1,sheet.nrows):
    print(sheet.cell(i,10).value)
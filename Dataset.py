# Reading an excel file using Python 
import xlrd 
  
# Give the location of the file 
loc = ("dataset.xls") 
  
# To open Workbook 
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
assumption1 = {}
assumption2 = {}
assumption3 = {} 
# For row 0 and column 0 

for i in range(0,60):
    assumption1[i+1] = int(sheet.cell_value(i+1,1))
for i in range(0,40):
    assumption2[i+1] = int(sheet.cell_value(i+1,3))
for i in range(0,20):
    assumption3[i+1] = int(sheet.cell_value(i+1,5))
dataset = [assumption1,assumption2,assumption3]
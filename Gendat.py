import xlwt 
import copy
import random
from random import shuffle
from collections import defaultdict
from xlwt import Workbook 
#Generate Dataset for each assumption
def genDataset(p1,r11,r12,p2,r21,r22,p3,r31,r32,n):
    assumption_one = []
    for i in range(0,n):
      if i >= 0 and i < p1*n:
        assumption_one.append(random.randint(r11,r12))
      elif i >= p1*n and i < (p1*n)+(p2*n):
        assumption_one.append(random.randint(r21,r22))
      else :
        assumption_one.append(random.randint(r31,r32))
                #########
                # queue in process
    random.shuffle(assumption_one)
    return mappingProcess(assumption_one)
def mappingProcess(Rawprocess):
    dataset = {}
    i =1
    for p in Rawprocess:
      dataset[i] = p
      i += 1
    return dataset
    
assumption1 = genDataset(0.7,2,8,0.2,20,30,0.1,35,40,60)
assumption2 = genDataset(0.5,2,8,0.3,20,30,0.2,35,40,40)
assumption3 = genDataset(0.4,2,8,0.4,20,30,0.2,35,40,20)
# Workbook is created 
wb = Workbook() 
  
# add_sheet is used to create sheet. 
sheet1 = wb.add_sheet('Sheet 1') 
sheet1.write(0, 0, 'Process') 
sheet1.write(0,1,'Burst Time')
sheet1.write(0, 2, 'Process') 
sheet1.write(0,3,'Burst Time')
sheet1.write(0, 4, 'Process') 
sheet1.write(0,5,'Burst Time')
for i in range(len(assumption1)):
    sheet1.write(i+1,0, int(i+1))
    sheet1.write(i+1,1,int(assumption1[i+1]))
for i in range(len(assumption2)):
    sheet1.write(i+1,2, int(i+1))
    sheet1.write(i+1,3,int(assumption2[i+1]))
for i in range(len(assumption3)):
    sheet1.write(i+1,4, int(i+1))
    sheet1.write(i+1,5,int(assumption3[i+1]))
wb.save('dataset.xls') 
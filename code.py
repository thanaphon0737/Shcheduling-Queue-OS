import random
import copy
from random import shuffle
from collections import defaultdict
import matplotlib.pyplot as plt
import numpy as np
from Dataset import dataset
def averageTime(process):
    n = len(process)
    w_time = 0
    for i in range(1,n+1):
      w_time += process[i]
    
    #Average waitingtime
    summary =0
    for i in range(1,n+1):
      summary += process[i]
    # print(process)
    # print("average time : %.2f ms" %(summary/n))
    return summary/n

def algorithm1(rawdata):
                #########
# Algorithm1 First-Come,First-Served(FCFS) Scheduling
    print("---algorithm1 First-Come,First-Served(FCFS) Scheduling---")
    start = 0
    end = 0
    s = defaultdict(list)
    e = defaultdict(list)
    data = copy.deepcopy(rawdata)
    for i in range(1,len(data)+1):
      s[i].append(start)    #find start and end for each process
      end = start + data[i]
      e[i].append(end)
      start = end
    n = len(s)
    sump = 0
    waitingset ={}
    for x in range(1,n+1):
      for y in range(len(s[x])):
        sump += e[x][y] - s[x][y]  #find waitingtime form end-start
      waitingset[x] = e[x][-1] - sump
      sump = 0
    turningset = {} #find turningtime  
    for i in range(1,n+1):
      turningset[i] = waitingset[i] + rawdata[i]
    # print("defalut dataset :")
    # print(data)
    # print("process queue :")
    # for i in range(1,len(data)+1):
    #   print("P[%d] : [%d -> %d]" %(i,s[i][0],e[i][0]))
    # print("wating time :")
    return [averageTime(turningset),averageTime(waitingset),s,e]
    print("---------------------------------------------------------")

def algorithm2(rawdata):
# Algorithm2 Shortest-Job-First(SJF) Scheduling
  print("---Algorithm2 Shortest-Job-First(SJF) Scheduling---")
  start = 0
  end = 0
  s = defaultdict(list)
  e = defaultdict(list)
  datalenght = len(rawdata)
  data1 = copy.deepcopy(rawdata)
  data = sorted(data1.values())
  datalist = {}
  for i in range(1,len(data)+1):
    datalist[i] = data[i-1]
  for i in range(1,len(datalist)+1):
    s[i].append(start)
    end = start + datalist[i]
    e[i].append(end)
    start = end

  # print("defalut dataset :")
  # print(data1)
  # print("process queue :")
  showval = []
  while len(data1) != 0:
    key_min = min(data1, key = lambda k: data1[k])  #find minTime of process for first queue
    value_min = data1[key_min]
    showval.append(key_min)
    del data1[key_min]
  stemp = copy.deepcopy(s)
  etemp = copy.deepcopy(e)
  for i in range(1,datalenght+1):
    # print("P[%d] : [%d -> %d]" %(showval[i-1],s[i][0],e[i][0]))
    stemp[showval[i-1]][0] =s[i][0] 
    etemp[showval[i-1]][0] = e[i][0]
  # print(stemp)
  # print(etemp)
  n = len(s)
  sump = 0
  waitingset ={}
  for x in range(1,n+1):
    for y in range(len(s[x])):
      sump += etemp[x][y] - stemp[x][y]
    waitingset[x] = etemp[x][-1] - sump
    sump = 0
  turningset = {}
  for i in range(1,n+1):
    turningset[i] = waitingset[i] + rawdata[i]
  # print("wating time :")
  return [averageTime(turningset),averageTime(waitingset),stemp,etemp]
  print("---------------------------------------------------------")

def algorithm3(rawdata,q = 8):
# Alforithm3 Round Robin(RR) Scheduling
    print("---Algorithm3 Round Robin(RR) Scheduling--")
    data = rawdata
    pre = copy.deepcopy(data)
    s = defaultdict(list)  
    e = defaultdict(list)
    start =0
    end =0
    count = 0
    while True:
      for i in range(1,len(pre)+1):
        if pre[i] != 0:         #pre is rawdata
          if pre[i]-q > 0:     
            pre[i] = pre[i] - q #find start and end of process
            end = start + q     #process will has burst time at most is q
          else:
            end = start + pre[i]
            pre[i] = 0
          starttemp = start
          start = end
          s[i].append(starttemp)
          e[i].append(end)
      for i in range(1,len(pre)+1):
        if pre[i] == 0:
          count += 1
      if count == len(pre):
        break
      count = 0
    n = len(s)
    sump = 0
    waitingset ={}
    for x in range(1,n+1):
      for y in range(len(s[x])):
        sump += e[x][y] - s[x][y]
      waitingset[x] = e[x][-1] - sump
      sump = 0
    turningset = {}
    for i in range(1,n+1):
      turningset[i] = waitingset[i] + rawdata[i]
    # print("defalut dataset :")
    # print(data)
    # print("process queue :")
    # for i in range(1,n+1):
    #   for j in range(len(s[i])):
    #     print("P[%d] : [%d -> %d]" %(i,s[i][j],e[i][j]))
    # print("wating time :")
    return [averageTime(turningset),averageTime(waitingset),s,e]
  
    print("---------------------------------------------------------")

def drawscheduling(start,end,label,label_qTime = ""):
  plotset_p = []
  plotset_e = []
  fig, ax = plt.subplots()
  for i in range(1,len(start)+1):
    for j in range(len(start[i])):
      plotset_e.append(tuple([start[i][j],end[i][j]-start[i][j]]))
    plotset_p.append(plotset_e)
    plotset_e = []
  p_count = len(plotset_p)
  init_y = 0
  margin = 10
  stepup = init_y
  stepsize = 1
  barsize = 1
  limx = 0
  for x in plotset_p:    
    ax.broken_barh(x, (stepup, barsize), facecolors='tab:blue')
    stepup += stepsize
    for y in x:
      if max(y) > limx :
        limx = max(y)
  ax.set_ylim(0, init_y+(stepsize*p_count))
  ax.set_xlim(0, limx+margin)
  ax.set_xlabel('time(ms)')
  ytick = np.arange(init_y,(init_y+(p_count-1)*stepsize)+stepsize,stepsize).tolist()
  ax.set_yticks(ytick)
  label_y = [1]
  for i in range(p_count):
    if i > 0 :
      if i % 10 == 0:
        label_y.append(str(i))
      else:
        label_y.append("")
  ax.set_yticklabels(label_y)
  ax.set_title(label + "Algorithm" + "\nScheduling of Process"+label_qTime)
  ax.set_ylabel('Processes')
  ax.grid(True)
  fig.tight_layout()
  plt.show()

def plotTurnaroundTime(rawdata1,rawdata2,rawdata3):
  algorlabel =['FCFS','SJF','RR']
  data1 = [round(algorithm1(rawdata1)[0],2),round(algorithm2(rawdata1)[0],2),round(algorithm3(rawdata1)[0],2)]
  data2 = [round(algorithm1(rawdata2)[0],2),round(algorithm2(rawdata2)[0],2),round(algorithm3(rawdata2)[0],2)]
  data3 = [round(algorithm1(rawdata3)[0],2),round(algorithm2(rawdata3)[0],2),round(algorithm3(rawdata3)[0],2)]
  x = np.arange(len(algorlabel))  # the label locations
  width = 0.25  # the width of the bars
  fig, ax = plt.subplots()
  rects1 = ax.barh(x + width, data1, width, label='Assumption1')
  rects2 = ax.barh(x, data2, width, label='Assumption2')
  rects3 = ax.barh(x - width, data3,width, label='Assumption3')
# Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_xlabel('Average Time(ms)')
  ax.set_title('Average Turnaround Time')
  ax.set_ylabel('Algorithm')
  ax.set_yticks(x)
  ax.set_yticklabels(algorlabel)
  ax.legend()
  def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        width = rect.get_width()
        ax.annotate('{}'.format(width),
                    xy=(width+0.75,rect.get_y()+rect.get_height()/4),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
  autolabel(rects1)
  autolabel(rects2)
  autolabel(rects3)
  fig.tight_layout()

  plt.show()

def plotWaitingTime(rawdata1,rawdata2,rawdata3):
  algorlabel =['FCFS','SJF','RR']
  data1 = [round(algorithm1(rawdata1)[1],2),round(algorithm2(rawdata1)[1],2),round(algorithm3(rawdata1)[1],2)]
  data2 = [round(algorithm1(rawdata2)[1],2),round(algorithm2(rawdata2)[1],2),round(algorithm3(rawdata2)[1],2)]
  data3 = [round(algorithm1(rawdata3)[1],2),round(algorithm2(rawdata3)[1],2),round(algorithm3(rawdata3)[1],2)]
  x = np.arange(len(algorlabel))  # the label locations
  width = 0.25  # the width of the bars
  fig, ax = plt.subplots()
  rects1 = ax.barh(x + width, data1, width, label='Assumption1')
  rects2 = ax.barh(x, data2, width, label='Assumption2')
  rects3 = ax.barh(x - width, data3,width, label='Assumption3')
# Add some text for labels, title and custom x-axis tick labels, etc.
  ax.set_xlabel('Average Time(ms)')
  ax.set_title('Average Waiting Time')
  ax.set_ylabel('Algorithm')
  ax.set_yticks(x)
  ax.set_yticklabels(algorlabel)
  ax.legend()
  def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        width = rect.get_width()
        ax.annotate('{}'.format(width),
                    xy=(width+0.75,rect.get_y()+rect.get_height()/4),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
  autolabel(rects1)
  autolabel(rects2)
  autolabel(rects3)
  fig.tight_layout()

  plt.show()
def plotroundrobin(rawdata):
  fig, axs = plt.subplots()
  a = copy.deepcopy(rawdata)
  turntimeset = []
  seti = []
  y_point = 999
  x_point = 0
  for i in range(40):
    turntimeset.append(algorithm3(a,i+1)[0])
    seti.append(i+1)
    if y_point > algorithm3(a,i+1)[0]:
      y_point = algorithm3(a,i+1)[0]
      x_point = i+1
  axs.grid(True)
  axs.plot(seti,turntimeset)
  axs.set_title('Turnaround Time Varies With The Time Quantum')
  axs.set_xlabel('time quantum')
  axs.set_ylabel('average turnaround time')
  axs.annotate('optimal q =' + str(x_point) +"\n"+str(round(y_point,2))+"ms",xy=(x_point,y_point),
            xytext=(0.8, 0.2), textcoords='axes fraction',
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=16,
            horizontalalignment='right', verticalalignment='top')
  plt.show()

  
def main():
  dataset1 = dataset[0]
  dataset2 = dataset[1]
  dataset3 = dataset[2]
  # for keep data
  # launch = dataset3
  # a = algorithm1(launch) #[TurningTime,WaitingTime,s,e]
  # b = algorithm2(launch)
  # c = algorithm3(launch,40)
  # drawscheduling(a[2],a[3],"First-come,First-served(FCFS)")
  # drawscheduling(b[2],b[3],"Shortest-Job-First(SJF)")
  # drawscheduling(c[2],c[3],"Round Robin(RR)"," \nquantum time = 40 ms")
  plotTurnaroundTime(dataset1,dataset2,dataset3)
  plotWaitingTime(dataset1,dataset2,dataset3)

# main()
plotroundrobin(dataset[1])
plotroundrobin(dataset[2])
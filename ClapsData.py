import csv
from numpy.core.fromnumeric import mean
import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random
import statistics

file=pd.read_csv('medium_data.csv')
data=file['claps'].tolist()

figure=ff.create_distplot([data],['claps'],show_hist=False)
figure.show()


list=[]

for i in range(0,30):
    randomIndex= random.randint(0,len(data)-1)
    value= data[randomIndex]
    list.append(value)

meanOfSampleData=statistics.mean(list)

print('mean Of Sample Data '+str(meanOfSampleData))


def dataOFRandomData(counter):
    createList=[]
    for i in range(0,counter):
     randomIndex= random.randint(0,len(data))
     value= data[randomIndex]
     createList.append(value)

    meanOfSampleData=statistics.mean(createList)
    
    return meanOfSampleData


def showFigure(data2):
    file=data2
    meanOfFile=statistics.mean(file)
    figure=ff.create_distplot([file],['claps'],show_hist=False)
    figure.add_trace(go.Scatter(x=[meanOfFile,meanOfFile],y=[0,0.05],mode='lines',name='Mean'))
    figure.show()



def setup():
    list=[]
    for i in range(0,100):
        randomData=dataOFRandomData(30)
        list.append(randomData)

    showFigure(list)
    mean=statistics.mean(list)
   

    print('mean Of Sampling Distribution '+str(mean))
   

setup()

 



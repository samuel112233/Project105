import csv
import pandas as pd 
import plotly.express as px
import math

with open('data.csv')as f:
    reader=csv.reader(f)
    fileData=list(reader)
#data=fileData[1]
def mean(data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
square_list=[]
for number in data:
    a=int(number)-mean(data)
    a=a**2
    square_list.append(a)
sum=0
for i in square_list  :
    sum=sum+i 
result=sum/(len(data)-1)
stdv=math.sqrt(result)
print(stdv)
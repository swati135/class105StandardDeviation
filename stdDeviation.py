import csv
import math
import plotly.express as px

fileData=[]
with open('class1.csv', newline='') as f:
    reader = csv.reader(f)
    fileData = list(reader)
    
fileData.pop(0)

def mean(data):
    n= len(data)
    total = 0
    for x in data:
        total+=(int(x))
        
    mean = total/n
    return mean
squared_list=[]

for num in fileData[1]:
    a= int(num) - mean(fileData[1])
    a=a**2
    squared_list.append(a)
    
sum = 0
for i in squared_list:  
    sum= sum+i

result = sum/len(fileData)
standardDeviation = math.sqrt(result)

print(standardDeviation)

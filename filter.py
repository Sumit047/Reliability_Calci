import pandas as pd
import statistics

import input
inp=input.inputs
a=inp.failures()
df=pd.read_csv(r'./files/output.csv')
t=df.Time_Interval.tolist()
rs=df.Reason_of_failure.tolist()
pof=df.Probability_of_Failure.tolist()
fr=df.Failure_Rate.tolist()
mtbf=df.Mean_Time_Between_Failures.tolist()
cf=df.Components_Failed.tolist()
sum=inp.total_failure(a)
fl=inp.filters(a,sum)

header=['Reason_of_failure','Components_Failed','Time_Interval','Failure_Rate','Mean_Time_Between_Failures']
data=[]
for i in range(len(t)):
    data.append([])
i=0
l=len(t)
md=statistics.median(fl)
j=0
while i<l:
    if fl[i]>md:
        data[j].append(rs[i])
        data[j].append(cf[i])
        data[j].append(t[i])
        data[j].append(fr[i])
        data[j].append(mtbf[i])
        j+=1
    i+=1

import output
wr=output.write_in
path = r'./files/filtered.csv'
wr.writrintofile(data,header,path)

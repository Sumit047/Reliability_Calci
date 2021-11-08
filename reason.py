import pandas as pd
import statistics
import input
inp=input.inputs
a=inp.failures()
df=pd.read_csv(r'./files/output.csv')
frequency = df['Reason_of_failure'].value_counts()

# print(frequency)
t=df.Time_Interval.tolist()
rs=df.Reason_of_failure.tolist()
pof=df.Probability_of_Failure.tolist()
fr=df.Failure_Rate.tolist()
sum=inp.total_failure(a)
fl=inp.filters(a,sum)
header=['Reason_of_failure']
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
        j+=1
    i+=1

i=0
l=len(frequency)
mdf=frequency.median()
while i<l:
    if frequency[i]>mdf:
        data[j].append(rs[j])
        j+=1
    i+=1
import output
wr=output.write_in
path = r'./files/reason.csv'
wr.writrintofile(data,header,path)
dfr=pd.read_csv(r'./files/reason.csv')
frequency = dfr['Reason_of_failure'].value_counts()
print(frequency)
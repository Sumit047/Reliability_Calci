import pandas as pd
import numpy as np
# import Reliability_Calculator 
# tp=Reliability_Calculator.file()
rl='input'
df = pd.read_csv(f'./files/{rl}.csv')
df.replace(r'\s+', np.nan, regex=True)
df = df.fillna(method='bfill')
class inputs:
    
        
    def compo():
        col=df.columns
        l=len(col)
        i=0
        com=0
        while i<l:
            if col[i]==f"Product{i-2}":
                com+=1
            i+=1
        return com
                
    def frange():
        r=df.Sr.tolist()
        return r
    
    def failures():
        a = df.Number_of_Failure.tolist()
        return a
    
    def total_failure(a):
        sum=0
        l=len(a)
        i=0
        while i<l:
            sum+=a[i]
            i+=1
        return sum
    
    def duration():
        t1 = df.Time_Interval.tolist()
        t2 = [i.split('-')[0] for i in t1]
        t = [i.split('.')[0] for i in t2]
        a=[float(x) for x in t]
        return a
    
    def reason():
        r=df.Reason_of_failure.tolist()
        return r
    
    def component_failed():
        cf=df.Components_Failed.tolist()
        return cf
    
    def diff_duration(t):
        dt=[]
        l=len(t)
        dt.append(t[1]-t[0])
        i=1
        while i<l:
            dt.append(t[i]-t[i-1])
            i+=1
        return dt
    
    def filters(a,sum):
        i=0
        l=len(a)
        fl=[]
        while i<l:
            fl.append(a[i]/sum)
            i+=1
        return fl
            
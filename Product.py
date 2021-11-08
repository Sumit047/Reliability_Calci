import pandas as pd
import numpy as np
import statistics as s
df=pd.read_csv(r'./files/product.csv')
df.replace(r'\s+', np.nan, regex=True)
df = df.fillna(method='bfill')
class inputsp:
    def item1():
        a = df.Item1.tolist()
        return a
    
    def item2():
        a = df.Item2.tolist()
        return a
    
    def item3():
        a = df.Item3.tolist()
        return a
    def item4():
        a = df.Item4.tolist()
        return a
    def item5():
        a = df.Item5.tolist()
        return a
    
class computation:
    def variance(it):
        t=s.stdev(it)
        return pow(t,2)
    def variance1(it):
        return df.var()['Item1']
    def variance2(it):
        return df.var()['Item2']
    def variance3(it):
        return df.var()['Item3']
    def variance4(it):
        return df.var()['Item4']
    def variance5(it):
        return df.var()['Item5']
        
    
    def total(it1,it2,it3,it4,it5):
        l=len(it1)
        i=0
        a=[]
        while i<l:
            a.append(it1[i]+it2[i]+it3[i]+it4[i]+it5[i])
            i+=1
        return a
    
    def net_reliability(k,v1,v2,v3,v4,v5,vt):
        sum=v1+v2+v3+v4+v5
        l=k/(k-1)
        return((vt-sum)/vt)
    
    def check_reliability(nr):
        if nr<0:
            return f"Wrong Entries"
        if nr>0 and nr<=0.2:
            return "Less Reliable"
        if nr>.2 and nr<=.4:
            return "Rather Reliable"
        if nr>.4 and nr<=.6:
            return "Quite Reliable"
        if nr>.6 and nr<=.8:
            return "Reliable"
        else:
            return "Very Reliable"
         
    def check_reliabilityq(nr):
        if nr<0:
            return ""
        if nr>0 and nr<=0.2:
            return "Very Poor"
        if nr>.2 and nr<=.4:
            return "Not Good "
        if nr>.4 and nr<=.6:
            return "Good"
        if nr>.6 and nr<=.8:
            return "Very Good"
        else:
            return "Excellent"   
import numpy as np
class computations:
    def failures_till_that_point(a):
        c=[]
        l=len(a)
        c.append(a[0])
        i = 1
        while i < l:
            c.append(c[i - 1] + a[i])
            i+= 1  
        return c
    def probability_of_failure(fttp,sum):
        pof=[]
        l=len(fttp)
        i=0
        while i<l:
            pof.append(round(fttp[i] / sum,2))
            i+=1
        return pof
    def failure_rate(a,avg_sc,t_df):
        fr=[]
        l=len(a)
        i=0
        while i<l:
            m=avg_sc[i]*t_df[i]
            r=a[i] / m
            fr.append(round(r,4))
            i+=1
        return fr
    def survivals(a,sum):
        sv=[]
        sv.append(sum-a[0])
        l=len(a)
        i=1
        while i<l:
            sv.append(sv[i-1]-a[i])
            i+=1
        return sv 
    def average_survivals(sv,sum):
        avg_sc=[]
        l=len(sv)
        avg_sc.append((sv[0]+sum)/2)
        i=1
        while i<l:
            avg_sc.append(float((sv[i]+sv[i-1])/2))
            i+=1
        return avg_sc
    def reliability_factor(pof):
        l=len(pof)
        i=0
        rf=[]
        while i<l:
            rf.append(round(1-pof[i],2))
            i+=1
        return rf
    def mtbf(sum,t):
        mt=[]
        i=0
        l=len(t)
        while i<l:
            mt.append(sum/t[i])
            i+=1
        return mt
    def mean_failure_rate(t):
        l=len(t)
        sum=0
        i=0
        while i<l:
            sum+=t[i]
            i+=1
        return sum
                

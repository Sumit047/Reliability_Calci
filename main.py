import input
import computation

# Input Dataframing

inp=input.inputs
comp=inp.compo()

#Input for multiple components

i=0
a=inp.failures()
sum=inp.total_failure(a)
t=inp.duration()
t_df=inp.diff_duration(t)
rang=inp.frange()
rs=inp.reason()
cf=inp.component_failed()

# Basic Computations

comp=computation.computations
fttp=comp.failures_till_that_point(a)
sv=comp.survivals(a,sum)
avg_sv=comp.average_survivals(sv,sum)
pof=comp.probability_of_failure(fttp,sum)
rf=comp.reliability_factor(pof)
fr=comp.failure_rate(a,avg_sv,t_df)
# comp.mtbf(rf,t)
mttf=comp.mean_failure_rate(t)
mtbf=comp.mtbf(t[len(t)-1]+t[1],fttp)



# Visualization

import visualisation
visual=visualisation.visualize
# pof=comp.probability_of_failure(fttp,sum)
rfs=visual.scatter_plot
rfb=visual.bar_graph
rfp=visual.pie_chart
# fr=comp.failure_rate(a,avg_sv,t_df)
class visualize:
    class reliability_factor:
        def scatter_plot():
            rfs.reliability_factor(rf,t)
        def bar_graph():
            rfb.reliability_factor(rf,t)
        def pie_chart():
            rfp.reliability_factor(rf,t)
    class failure_rate:
        def scatter_plot():
            rfs.failure_rate(fr,t)
        def bar_graph():
            rfb.failure_rate(fr,t)
        def pie_chart():
            rfp.failure_rate(fr,t)
    class probability_of_failure:
        def scatter_plot():
            rfs.probability_of_failure(rf,t)
        def bar_graph():
            rfb.probability_of_failure(rf,t)
        def pie_chart():
            rfp.probability_of_failure(rf,t)
    class mtbf:
        def scatter_plot():
            rfs.mean_time_between_faiures(rf,t)
        def bar_graph():
            rfb.mean_time_between_faiures(rf,t)
        def pie_chart():
            rfp.mean_time_between_faiures(rf,t)
            
            

# Write in to output file

import output
wr=output.write_in
header=['Sr. No.','Reason_of_failure','Components_Failed','Number_of_failures','Time_Interval','Reliability_Factor','Probability_of_Failure','Failure_Rate','Mean_Time_Between_Failures']
data=[]
for i in range(len(a)):
    data.append([])
i=0
l=len(a)
while i<l:
    data[i].append(rang[i])
    data[i].append(rs[i])
    data[i].append(cf[i])
    data[i].append(a[i])
    data[i].append(t[i])
    data[i].append(rf[i])
    data[i].append(pof[i])
    data[i].append(fr[i])
    data[i].append(mtbf[i])
    i+=1
path = r'./files/output.csv'
wr.writrintofile(data,header,path)


# Predict Out the values

import Prediction_model
pm=Prediction_model.predict
pm_rf=pm.reliability_factor
pm_fr=pm.failure_rate
pm_pof=pm.probability_of_failure
pm_mtbf=pm.mean_time_between_faiures
class Predict:
    def reliability_factor(val):
        pm_rf.calculate(rf,t,val)
    def failure_rate(val):
        pm_fr.calculate(fr,t,val)
    def probability_of_failure(val):
        pm_pof.calculate(pof,t,val)
    def mtbf(val):
        pm_mtbf.calculate(mtbf,t,val)
                                
import numpy as np
class predict:
    class reliability_factor:
        def calculate(rf,t,val):
            x = np.array(t)
            y = np.array(rf)
            z = np.polyfit(x, y, 3)
            p = np.poly1d(z)
            print(round(p(val),3))
            
    class failure_rate:
        def calculate(fr,t,val):
            x = np.array(t)
            y = np.array(fr)
            z = np.polyfit(x, y, 3)
            p = np.poly1d(z)
            print(p(val))            
            
    class probability_of_failure:
        def calculate(pof,t,val):
            x = np.array(t)
            y = np.array(pof)
            z = np.polyfit(x, y, 3)
            p = np.poly1d(z)
            print(p(val))     
            
    class mean_time_between_faiures:
        def calculate(mtbf,t,val):
            x = np.array(t)
            y = np.array(mtbf)
            z = np.polyfit(x, y, 3)
            p = np.poly1d(z)
            print(p(val))            
                       
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (15,7)


def rfs():
        plt.title("Reliability Factor",fontsize=30)
        plt.xlabel("---------Time Taken--------->",fontsize=20)
        plt.ylabel("---------Reliability Factor--------->",fontsize=20)
        
def frs():
        plt.title("Failure Rate",fontsize=30)
        plt.xlabel("---------Time Taken--------->",fontsize=20)
        plt.ylabel("---------Failure Rate--------->",fontsize=20)
def pofs():
        plt.title("Probability of Failure",fontsize=30)
        plt.xlabel("---------Time Taken--------->",fontsize=20)
        plt.ylabel("---------Probability of Failure--------->",fontsize=20)
def mtbfs():
        plt.title("Mean Time Between Failures",fontsize=30)
        plt.xlabel("---------Time Taken--------->",fontsize=20)
        plt.ylabel("---------Mean Time Between Failures--------->",fontsize=20)    

class visualize:
    class bar_graph:
        def reliability_factor(rf,t):
            rfs()
            plt.bar(t, rf,color='green')
            plt.show()
        def failure_rate(fr,t):
            frs()
            plt.bar(t, fr,color='red')
            plt.show()
        def probability_of_failure(pof,t):
            pofs()
            plt.bar(t, pof,color='orange')
            plt.show()
        def mean_time_between_faiures(mtbf,t):
            mtbfs()
            plt.bar(t, mtbf,color='orange')
            plt.show()
            

    class scatter_plot:
        def reliability_factor(rf,t):
            rfs()
            plt.scatter(t, rf,color='green')
            plt.plot(t,rf,color='green')
            plt.show()
        def failure_rate(fr,t):
            frs()
            plt.scatter(t, fr,color='red')
            plt.plot(t,fr,color='red')
            plt.show()
        def probability_of_failure(pof,t):
            pofs()
            plt.scatter(t, pof,color='orange')
            plt.plot(t,pof,color='orange')
            plt.show()
        def mean_time_between_faiures(mtbf,t):
            mtbfs()
            plt.scatter(t, mtbf,color='orange')
            plt.plot(t,mtbf,color='orange')
            plt.show()


    class pie_chart:
        def reliability_factor(rf,t):
            plt.pie(t,rf,labels=rf)
            plt.legend(title="Reliability Factor",loc=4)
            plt.show()

        def failure_rate(fr,t):
            plt.pie(t,fr,labels=fr)
            plt.legend(title="Failure rate",loc=4)
            plt.show()

        def probability_of_failure(pof,t):
            plt.pie(t,pof,labels=pof)
            plt.legend(title="Probability Of Failure",loc=4)
            plt.show()

        def mean_time_between_faiures(mtbf,t):
            plt.pie(t,mtbf,labels=mtbf)
            plt.legend(title="Mean Time Between Failures",loc=4)
            plt.show()









import random 
import plotly.express as px 
import plotly.figure_factory as ff
import csv 
import pandas as pd 
import statistics
import random
import plotly.graph_objects as go


df =pd.read_csv("medium_data.csv")
data=df["reading_time"].tolist()
mean=statistics.mean(data)
#print(mean)

stdev=statistics.stdev(data)
print(stdev)

# To take random numbers
dataSet=[]
for i in range(0,30):
    index=random.randint(0,len(data))
    value=data[index]
    dataSet.append(value)
mean=statistics.mean(dataSet)
print(mean)
stdev=statistics.stdev(dataSet)
print(stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

#function to plot the mean on the graph
def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=True)
    fig.show()


# Pass the number of time you want the mean of the data points as a parameter in range function in for loop
def setup():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    
    mean = statistics.mean(mean_list)
    print("Mean of sampling distribution :-",mean )

setup

#Code to find the mean of the raw data ("population data")
population_mean = statistics.mean(data)
print("population mean:- ", population_mean)

# code to find the standard deviation of the sample data
def standard_deviation():
    mean_list = []
    for i in range(0,1000):
        set_of_means= random_set_of_mean(100)
        mean_list.append(set_of_means)

    std_deviation = statistics.stdev(mean_list)
    print("Standard deviation of sampling distribution:- ", std_deviation)

standard_deviation()

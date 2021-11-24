import plotly.figure_factory as ff
import csv
import pandas as pd
import statistics
import random

df = pd.read_csv("newdata.csv")

data = df["average"].tolist()

#fig = ff.create_distplot([data], ["average"], show_hist = False)
#fig.show()

meanofpopulation = statistics.mean(data)
medianofpopulation = statistics.median(data)
modeofpopulation = statistics.mode(data)
print(meanofpopulation, medianofpopulation, modeofpopulation)

def experiment(): 
    samples = []
    for i in range(100): 
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        samples.append(value)
    meanofsamples = statistics.mean(samples)
    return(meanofsamples)

meanfromexperiments = []
for i in range(700):
    meanofsamples = experiment()
    meanfromexperiments.append(meanofsamples)

mean = statistics.mean(meanfromexperiments)
median = statistics.median(meanfromexperiments)
mode = statistics.mode(meanfromexperiments)

print(mean, median, mode)

fig = ff.create_distplot([meanfromexperiments], ["Sampling average"], show_hist = False)
fig.show()

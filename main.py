import random
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv 

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

#fig = ff.create_distplot([data], ["temp"], show_hist=False)
#fig.show()


def experiment():
    samples = []
    for i in range(100):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        samples.append(value)
    
    meanofsamples = statistics.mean(samples)
    return meanofsamples

meanfromexperiments = []
for i in range(1000):
    meanofsamples = experiment()
    meanfromexperiments.append(meanofsamples)


mean = statistics.mean(meanfromexperiments)
mode = statistics.mode(meanfromexperiments)
median = statistics.median(meanfromexperiments)

print(mean, median, mode)

fig = ff.create_distplot([meanfromexperiments], ["Sampling"], show_hist=False)
fig.show()


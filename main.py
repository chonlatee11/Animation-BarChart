from cProfile import label
from calendar import different_locale
from tracemalloc import stop
from turtle import color
from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

years = [str(1960 + i) for i in range(61)]
countries = ["Myanmar" , "Thailand" , "Malaysia" , "Indonesia" , "Philippines" , "Singapore" , "Vietnam" , "Lao PDR" , "Cambodia" , "Brunei Darussalam"]
df = pd.read_csv('gdp.csv')

df = df.query("`Country Name` == @countries")
#print(df)
countries = df['Country Name']

df = df[["Country Name"] + years].dropna(axis=1)

data = np.empty((1 , 10))

for year in df.columns[1:]:
    data = np.append(data , [df[year].to_numpy()] , 0)

#print(data)
plot_steps = np.array([data[0]])
last_gdp = data[0]
for i in range(1 , len(data)):
    differences = data[i] - last_gdp
    differences /= 100
    for j in range(100):
        plot_steps = np.append(plot_steps , [last_gdp + differences * j] , 0)
    last_gdp = data[i]

colors = ["#ff8888" , "#ff22dd" , "#5555ff" , "#55ccff" , "#ffaa55" , "#ff55ff" , "#ffdd22" , "#ff5622" ,"#2211dd" , "#334411"]
years = iter(df.columns[1:])
for i , step in enumerate(plot_steps):
    if i % 100 == 0:
        try :
            year = next(years)
        except StopIteration:
            pass
    list_sorted = step.copy()
    list_sorted.sort()
    
    list_index = []
    for x in list_sorted:
        list_index.insert(0 , list(step).index(x))
        
    country_names = df['Country Name'].to_numpy()
    ordered_names = [country_names[i] for i in list_index]
    ordered_colors = [colors[i] for i in list_index]
    
    plt.title("GDP Per Capita Asian")
    plt.barh(ordered_names[::-1] , list_sorted , color = ordered_colors[::-1])
    plt.text(50000 , 0.2 , year , fontsize = 18)
    plt.xlim(0 , 120000)
    plt.pause(0.001)
    plt.clf()
plt.show()


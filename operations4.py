import data
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

petrol_ele = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-Electric"] # selecting data of given fuel type
petrol_cng = data.pop_data[data.pop_data["Fuel Type"]== "Petrol-CNG"]
x =[0,0,0,0,0,0,0,0,0,0,0,0,0]
x1 =[0,0,0,0,0,0,0,0,0,0,0,0,0]
y = [2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018]


def line_plot():
    print("Difference between Petrol-Electric and Petrol-CNG vehicle population (for each Year) vs Year as a line plot")

    plt.figure(figsize=(14,8))
    plt.title('Difference between Petrol-Electric and Petrol-CNG vehicle population (for each Year) vs Year as a line plot')




    for i in range(1,14):
        for year, pvalue in petrol_ele.iterrows() :



            for year, cvalue in petrol_cng.iterrows():
                x[i-1] = (pvalue[i]-cvalue[i])


    plt.plot(x,y, color ='red',linestyle='dashed')

    plt.xlabel('Difference between Petrol-Electric and Petrol-CNG')
    plt.ylabel('Year')
    plt.show()

def bar_plot():
    x_labels =['Petrol-Electric','Petrol-CNG']
    # Set plot parameters
    bwidth = 4 # width of bar

    fig = plt.subplots(figsize =(12, 8))

    for i in range(1,14):
        for year, pvalue in petrol_ele.iterrows() :
            x[i-1]=pvalue[i]

        for year ,cvalue in petrol_cng.iterrows():
            x1[i-1]=cvalue[i]


#plotting
    plt.bar(y,x,width =0.2 ,color ='red',edgecolor ='grey',label='Petrol-Electric')
    plt.bar(y,x1,width =0.2,color ='yellow',edgecolor ='grey',label ='Petrol-CNG')
    plt.ylabel('Population')
    plt.xlabel('Year' )
    plt.title('Vehicle Population of Petrol-CNG, Petrol-Electric ')
    plt.legend()
    plt.show()

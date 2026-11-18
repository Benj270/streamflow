# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np


#Create and slice array for Provo River
data=np.loadtxt('June-2021-Provo-River-Streamflow-Rates.csv',delimiter=',',skiprows=1,dtype=str)

x=data[:,0].astype('datetime64[m]') #date with minute presicion
y_1=data[:,1].astype('float') #site 10163000
y_2=data[:,2].astype('float') #site 10155200
y_3=data[:,3].astype('float') #site 10155500
y_4=data[:,4].astype('float') #site 10154200
y_5=data[:,5].astype('float') #site 10155000


#create the Provo River graph
plt.plot(x,y_1,label='Site 10163000',color='purple')
plt.plot(x,y_2,label='Site 10155200',color='teal')
plt.plot(x,y_3,label='Site 10155500',color='green')
plt.plot(x,y_4,label='Site 10154200',color='gold')
plt.plot(x,y_5,label='Site 10155000',color='red')

plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')
plt.title('Provo River Streamflow Data (2021)')
plt.legend(title='Site Numbers')
plt.xticks(rotation=45)
plt.grid()
plt.show()

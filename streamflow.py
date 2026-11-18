# -*- coding: utf-8 -*-
from fileinput import filename

import matplotlib.pyplot as plt
import numpy as np

def load_streamflow(filename):
    """
    Read the streamflow CSV. Return the dates and a 2D array of flows (cfs), one column per gauge."""
    data=np.loadtxt(filename,delimiter=',',skiprows=1,dtype=str)

    dates = data[:,0].astype('datetime64[m]')
    flows = data[:,1:6].astype(float)

    return dates, flows

def plot_streamflow(dates, flows, sites):
    """Plot the flow at each gauge, with the same title, labels, and formatting as the Matplotlib HW
    """
    colors=['purple', 'teal', 'green', 'goldenrod', 'red']
    for i in range(len(sites)):
        plt.plot(dates, flows[:,i], label=sites[i], color=colors[i])
    plt.xlabel('Date')
    plt.ylabel('Flowrate (cfs)')
    plt.title('Provo River Streamflow Data (2021)')
    plt.legend(title='Site Numbers')
    plt.xticks(rotation=45)
    plt.grid()
    plt.show()

sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
plot_streamflow(dates, flows, sites)
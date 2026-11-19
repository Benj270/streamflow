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
    plt.savefig("provo_streamflow.png", dpi=150, bbox_inches="tight")
    plt.show()

#Excel Check for 10163000:Max = 131.0 , Avg= 56.95, min = 35.6
def summarize(dates, flows, sites):
    """Print and save max, min, and average flow for each gauge to a csv file."""
    print("Gauge       Max (cfs)   Date of Max    Min(cfs)   Avg (cfs)")
    file = open("streamflow_summary.csv", "w")
    file.write("Gauge,Max (cfs),Date of Max,Min(cfs),Avg (cfs)\n")
    for i in range(len(sites)):
        flow = flows[:,i]
        max_flow = np.max(flow)
        min_flow = np.min(flow)
        avg_flow = np.mean(flow)
        max_row = np.argmax(flow)
        max_date = dates[max_row]
        print(f"{sites[i]} {max_flow:10.1f} {max_date} {min_flow:10.1f} {avg_flow:10.1f}")
        file.write(f"{sites[i]},{max_flow:.1f},{max_date},{min_flow:.1f},{avg_flow:.1f}\n")
    file.close()
sites = ["10163000", "10155200", "10155500", "10154200", "10155000"]
dates, flows = load_streamflow("June-2021-Provo-River-Streamflow-Rates.csv")
summarize(dates, flows, sites)
plot_streamflow(dates, flows, sites)

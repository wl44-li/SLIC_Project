import matplotlib.pyplot as plt
import os
import numpy as np

# Assume data is refined and baselined
def graph(data, filepath):
    
    filename = os.path.splitext(filepath)[0]
    
    ax_sec = data.plot()
    
    # Name axis
    ax_sec.set_xlabel("Time(sec)")
    ax_sec.set_ylabel("Growth(dB)")
    
    fig = ax_sec.get_figure()
    
    # set graph size
    fig.set_size_inches(16, 9)    
    
    # save graph to data directory
    fig.savefig(filename + '_fig.png', dpi = 100)
    
    # Plot data every 60 seconds (min interval)
    df = data[data.index % 60 == 0]
    df = df.reset_index(drop = True)
    
    ax = df.plot()
        
    fig = ax.get_figure()

    # Name axis
    ax.set_xlabel("Time(min)")
    ax.set_ylabel("Growth(dB)") 

    # set graph size
    fig.set_size_inches(16, 9)    
    
    # save graph to data directory
    fig.savefig(filename + '_fig_min.png', dpi = 100)
    
    # show on console (DEBUG purpose)
    plt.show()
    

# threshold is a number between 0 to 1
def thresholdGraph(data, threshold, filepath):
    filename = os.path.splitext(filepath)[0]

    # Plot data every 60 seconds
    df = data[data.index % 60 == 0]
    df = df.reset_index(drop = True)
    ax = df.plot()
    
    # control channel scatter
    ax_ctrl = df.reset_index().plot(x = 'index', y = 1, kind = 'scatter', ax = ax, c = "b")
    
    for i in range(2, len(df.columns) + 1):
        
        # above threashold RED, below GREEN
        colors = np.where(df['Channel ' + str(i-1)] > df['Control']*threshold, 'r', 'g')
        ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")
    
    ax.set_xlabel("Time(min)")
    ax.set_ylabel("Growth(dB)") 
    fig = ax.get_figure()
    fig.set_size_inches(16, 9)
    
    fig.savefig(filename + '_'+ (str)(threshold) + '_threshold.png', dpi = 100)

    plt.show()    


    
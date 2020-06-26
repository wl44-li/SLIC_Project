import matplotlib.pyplot as plt
import os
import numpy as np

# Assume data is refined and baselined
def graph(data, filepath):
    
    # save graph to same directory as raw data
    filename = os.path.splitext(filepath)[0]
    
    # default graph (seconds)
    ax_sec = data.plot()
    ax_sec.set_xlabel("Time(sec)")
    ax_sec.set_ylabel("Growth(dB)")
    
    fig = ax_sec.get_figure()
    
    # set graph size for better full-screen view
    fig.set_size_inches(16, 9)    
    
    # save graph to data directory
    fig.savefig(filename + '_fig.png', dpi = 120)
    
    # Plot data every 60 seconds (minute interval)
    df = data[data.index % 60 == 0]
    df = df.reset_index(drop = True)
    
    ax = df.plot()
    fig = ax.get_figure()
    ax.set_xlabel("Time(min)")
    ax.set_ylabel("Growth(dB)") 

    # set graph size
    fig.set_size_inches(16, 9)    
    
    # save graph to data directory
    fig.savefig(filename + '_fig_min.png', dpi = 120)
    
    # show on console (DEBUG purpose)
    plt.show()
    

# threshold is a number between 0 to 1 or % between 0 to 100
def thresholdGraph(data, threshold, title, filepath):
    
    if (threshold > 1 or threshold < 0):
        print("Invalid threshold, must be a number between 0 to 1")
        return None
    
    else:    
        filename = os.path.splitext(filepath)[0]
    
        # Plot data every 60 seconds
        df = data[data.index % 60 == 0]
        df = df.reset_index(drop = True)
        ax = df.plot()
        
        # control channel scatter blue
        ax_ctrl = df.reset_index().plot(x = 'index', y = 1, kind = 'scatter', ax = ax, c = "b")
        
        # scatter other columns one by one
        for i in range(2, len(df.columns) + 1):
            # above threashold is RED, below is GREEN
            colors = np.where(df.iloc[:, (i-1)] > df.iloc[:, 0]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")
        
        # graph title can be added via GUI 
        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
        fig = ax.get_figure()
        fig.set_size_inches(16, 9)
        
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120)
    
        plt.show()    


    
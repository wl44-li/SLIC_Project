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
        
        # backhground is a minute inteval graph
        ax = df.plot()
        
        # control channel scatter blue
        ax_ctrl = df.reset_index().plot(x = 'index', y = 1, kind = 'scatter', ax = ax, c = "b")
        
        time_tick = []
        # scatter other columns one by one
        for i in range(2, len(df.columns) + 1):
            
            green_list = df.iloc[:, (i-1)][df.iloc[:, (i-1)] < df.iloc[:, 0]*threshold].index.tolist()
            
            # Some discussion needed for first colour shift classification
            print("Channel :", i-1)
            print(green_list)
            print("\n")
            
            # above threashold is RED, below is GREEN
            colors = np.where(df.iloc[:, (i-1)] > df.iloc[:, 0]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")
            
            # Consecutive shift of 10 minutes 
            if (len(green_list) > 10):
                for i in range(0, len(green_list) - 10):
                    if (green_list[i] + 10 - 1 == green_list[i + 10 - 1]):
                        time_tick.append(green_list[i])
                        break
            else:
                time_tick.append('No valid colour shift detected')
                
        # set axis
        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        
        # set graph legend
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        
        # set graph title
        ax.title.set_text(title)
        
        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)):
            txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i+1] + ' at ' + str(time_tick[i]) + " minute\n"
     
        fig = ax.get_figure()
        fig.text(0.95, 0.05, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.5))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120)
        
        plt.show()    

def threshold_errorbar(data, error, threshold, title, filepath):
    if (threshold > 1 or threshold < 0):
        print("Invalid threshold, must be a number between 0 to 1")
        return None
    
    else:    
        filename = os.path.splitext(filepath)[0]
    
        # Plot data every 60 seconds
        df = data[data.index % 60 == 0]
        df = df.reset_index(drop = True)
        
        df_err = error[error.index % 60 == 0]
        df_err = df_err.reset_index(drop = True)

        # backhground is a minute inteval graph
        ax = df.plot(yerr = df_err, linestyle = '-', linewidth = 0.5)
        
        # control channel scatter blue
        ax_ctrl = df.reset_index().plot(x = 'index', y = 1, kind = 'scatter', ax = ax, c = "b")
        
        time_tick = []
        
        # scatter other columns one by one
        for i in range(2, len(df.columns) + 1):
            
            green_list = df.iloc[:, (i-1)][df.iloc[:, (i-1)] < df.iloc[:, 0]*threshold].index.tolist()
            
            # above threashold is RED, below is GREEN
            colors = np.where(df.iloc[:, (i-1)] > df.iloc[:, 0]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "x")
            
            if (len(green_list) > 10):
                for i in range(0, len(green_list) - 10):
                    if (green_list[i] + 10 - 1 == green_list[i + 10 - 1]):
                        time_tick.append(green_list[i])
                        break
            else:
                time_tick.append('No valid colour shift detected')

        # set axis
        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        
        # set graph legend
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        
        # set graph title
        ax.title.set_text(title)
        
        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)):
            if (isinstance(time_tick[i], int)) :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i+1] + ' at ' + str(time_tick[i]) + " minute\n"
            else:
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i+1] + ' ' + time_tick[i] + ' \n'
                
        fig = ax.get_figure()
        
        fig.text(0.95, 0.05, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.5))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120)
        
        plt.show() 
    
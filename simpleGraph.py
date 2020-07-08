import matplotlib.pyplot as plt
import os
import numpy as np

''' Functions to produce graphs from dataframes
'''
def graph(data, filepath):
    # save graph to same directory as raw data
    filename = os.path.splitext(filepath)[0]

    # default graph (seconds)
    ax_sec = data.plot()
    ax_sec.set_xlabel("Time(sec)")
    ax_sec.set_ylabel("Growth(dB)")
    fig = ax_sec.get_figure()
    fig.set_size_inches(16, 9)
    fig.savefig(filename + 'sec_fig.png', dpi = 120)

    # Plot data every 60 seconds (minute interval)
    df = data.groupby(np.arange(len(data))//60).mean()
    ax = df.plot()
    fig = ax.get_figure()
    ax.set_xlabel("Time(min)")
    ax.set_ylabel("Growth(dB)")
    fig.set_size_inches(16, 9)
    fig.savefig(filename + 'min_fig.png', dpi = 120)
    
    # show on console (DEBUG purpose)
    plt.show()


# threshold is a % between 0 to 100 taken from GUI
def thresholdGraph(data, threshold, title, filepath):
    if (threshold > 1 or threshold < 0):
        print("Invalid threshold, must be a number between 0 to 1")
        return None

    else:
        filename = os.path.splitext(filepath)[0]
        
        # Plot data every 60 seconds (rolling average)
        df = data.groupby(np.arange(len(data))//60).mean()
        df.to_csv("clean.csv", index = False)
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = 1, kind = 'scatter', ax = ax, c = "b")

        time_tick = []
        # scatter other columns one by one
        for i in range(2, len(df.columns) + 1):
            green_list = df.iloc[:, (i - 1)][df.iloc[:, (i-1)] < df.iloc[:, 0] * threshold].index.tolist()

            # above threashold is coloured RED, below is GREEN
            colors = np.where(df.iloc[:, (i-1)] > df.iloc[:, 0]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

            # Consecutive shift of 2 minute (120 seconds)
            if (len(green_list) > 5):
                for i in range(0, len(green_list) - 2):
                    if (green_list[i] + 2 == green_list[i + 2]):
                        time_tick.append(green_list[i])
                        break
            else:
                time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)

        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)):
            if (isinstance(time_tick[i], int)) :
                if (i < len(time_tick) - 1):
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i+1] + ' at ' + str(time_tick[i]) + " minute\n"
                else:
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i+1] + ' at ' + str(time_tick[i]) + " minute"
            else:
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i+1] + ' ' + time_tick[i] + ' \n'
        
        fig = ax.get_figure()
        fig.text(0.45, -0.05, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.4))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120, bbox_inches = "tight")

        # Zoom in graph to 60 mins mark
        ax_zoom = ax
        ax_zoom.set_xlim([0, 60])
        ax_zoom.set_ylim([-1, 2.5])
        fig = ax_zoom.get_figure()
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_60min.png', dpi = 120, bbox_inches = "tight")
        plt.show()


# Support error bars with threshold_graph
def threshold_errorbar(data, error, threshold, title, filepath):
    if (threshold > 1 or threshold < 0):
        print("Invalid threshold, must be a number between 0 to 1")
        return None
    else:
        filename = os.path.splitext(filepath)[0]
        df = data.groupby(np.arange(len(data))//60).mean()

        df_err = error[error.index % 60 == 0]
        df_err = df_err.reset_index(drop = True)
        ax = df.plot(yerr = df_err, linestyle = '-', linewidth = 0.8)
        ax_ctrl = df.reset_index().plot(x = 'index', y = 1, kind = 'scatter', ax = ax, c = "b")
        time_tick = []

        # scatter other columns one by one
        for i in range(2, len(df.columns) + 1):
            green_list = df.iloc[:, (i-1)][df.iloc[:, (i-1)] < df.iloc[:, 0]*threshold].index.tolist()

            # above threashold is RED, below is GREEN
            colors = np.where(df.iloc[:, (i-1)] > df.iloc[:, 0]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = ".")

            if (len(green_list) > 5):
                for i in range(0, len(green_list) - 2):
                    if (green_list[i] + 2 == green_list[i + 2]):
                        time_tick.append(green_list[i])
                        break
            else:
                time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)

        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)):
            if (isinstance(time_tick[i], int)) :
                if (i < len(time_tick) - 1):
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i + 1] + ' at ' + str(time_tick[i]) + " minute\n"
                else:
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i + 1] + ' at ' + str(time_tick[i]) + " minute"
            else:
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i + 1] + ' ' + time_tick[i] + ' \n'

        fig = ax.get_figure()
        fig.text(0.45, -0.05, txt, ha = 'left', bbox = dict(facecolor = 'red', alpha = 0.4))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120, bbox_inches = "tight")
                
        # Zoom in graph to 60 mins mark
        ax_zoom = ax
        ax_zoom.set_xlim([0, 60])
        ax_zoom.set_ylim([-1, 2.5])
        fig = ax_zoom.get_figure()
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_60min.png', dpi = 120, bbox_inches = "tight")
        plt.show()


import matplotlib.pyplot as plt
import os
import numpy as np

def threshold_final(df, threshold, title, filepath, ctrl_num, isShow, isCondense):
    filename = os.path.splitext(filepath)[0]
    if (isCondense) :
        df = df.groupby(np.arange(len(df))//60).mean()
        print("Data condensed")
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num - 1) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) >= 10) :
                    for j in range(2, len(green_list) - 10) :
                        if (green_list[j] + 9 == green_list[j + 9]) :
                            time_tick.append(green_list[j])
                            break
                else :
                    time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
    
        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)) :
            if (i + 1 == ctrl_num) :
                txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                
            elif (isinstance(time_tick[i], int) and i != (ctrl_num - 1)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'
                        
        fig = ax.get_figure()
        if (isShow) :
            fig.text(0.45, -0.06, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.35))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_min.png', dpi = 120, bbox_inches = "tight")
        
    else:
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num - 1) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, 0]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) > 600) :
                    for j in range(2, len(green_list) - 100) :
                        if (green_list[j] + 90 == green_list[j + 90]) :
                            time_tick.append(green_list[j])
                            break
                else :
                    time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(sec)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)) :
            if (i + 1 == ctrl_num) :
                txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                
            elif (isinstance(time_tick[i], int) and i != (ctrl_num - 1)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'
                        
        fig = ax.get_figure()
        if (isShow) :
            fig.text(0.45, -0.08, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.35))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120, bbox_inches = "tight")
         
def threshold_zoom(df, threshold, title, filepath, ctrl_num, isShow, isCondense, xmax, xmin, ymax, ymin):
    filename = os.path.splitext(filepath)[0]
    if (isCondense) :
        df = df.groupby(np.arange(len(df))//60).mean()
        print("Data condensed")
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num - 1) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) >= 10) :
                    for j in range(2, len(green_list) - 10) :
                        if (green_list[j] + 9 == green_list[j + 9]) :
                            time_tick.append(green_list[j])
                            break
                else :
                    time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(min)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
    
        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)) :
            if (i + 1 == ctrl_num) :
                txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                
            if (isinstance(time_tick[i], int) and i != (ctrl_num - 1)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'
                        
        fig = ax.get_figure()
        fig.set_size_inches(16, 9, forward = True)

        if (isShow) :
            fig.text(0.45, -0.06, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.35))
        ax_zoom = ax
        ax_zoom.set_xlim([xmin, xmax])
        ax_zoom.set_ylim([ymin, ymax])
        fig = ax_zoom.get_figure()
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_min_zoom.png', dpi = 120, bbox_inches = "tight")
        plt.show()
        
    else:
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
    
        print("number of columns", len(df.columns))
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num - 1) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, 0]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) > 600) :
                    for j in range(2, len(green_list) - 100) :
                        if (green_list[j] + 90 == green_list[j + 90]) :
                            time_tick.append(green_list[j])
                            break
                else :
                    time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(sec)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
        txt = 'Colour shift info: \n'
        for i in range (0, len(time_tick)) :
            if (i + 1 == ctrl_num) :
                txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                
            if (isinstance(time_tick[i], int) and i != (ctrl_num - 1)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'
                        
        fig = ax.get_figure()
        fig.set_size_inches(16, 9, forward = True)

        if (isShow) :
            fig.text(0.45, -0.06, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.35))
    
        ax_zoom = ax
        ax_zoom.set_xlim([xmin, xmax])
        ax_zoom.set_ylim([ymin, ymax])
        fig = ax_zoom.get_figure()
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_zoom.png', dpi = 120, bbox_inches = "tight")
        plt.show()

def threshold_errorbar(df, error, threshold, title, filepath, ctrl_num, isShow, isCondense):
    filename = os.path.splitext(filepath)[0]
    if (isCondense) :
        df = df.groupby(np.arange(len(df))//60).mean()
        error = error[error.index % 60 == 0]
        error = error.reset_index(drop = True)
        print("Data condensed")     
    ax = df.plot(yerr = error, linestyle = '-', linewidth = 0.75)
    ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
    time_tick = []

    for i in range(1, len(df.columns) + 1) :
        if (i != ctrl_num - 1) :
            green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
            colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = ".")
            if (isCondense) :
                if (len(green_list) >= 10) :
                    for i in range(2, len(green_list) - 10) :
                        if (green_list[i] + 9 == green_list[i + 9]) :
                            time_tick.append(green_list[i])
                            break
                else :
                    time_tick.append('No valid colour shift detected')
            else :
                if (len(green_list) > 600) :
                    for i in range(2, len(green_list) - 100) :
                        if (green_list[i] + 90 == green_list[i + 90]) :
                            time_tick.append(green_list[i])
                            break
                else :
                    time_tick.append('No valid colour shift detected')
    
    if (isCondense) :
        ax.set_xlabel("Time(min)")
    else :
        ax.set_xlabel("Time(sec)")

    ax.set_ylabel("Growth(dB)")
    ax.legend(title = (str)(threshold * 100) + " % threshold")
    ax.title.set_text(title)
    txt = 'Colour shift info: \n'
    for i in range (0, len(time_tick)) :
        if (i + 1 == ctrl_num) :
            txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                
        if (i != (ctrl_num - 1) and isCondense == True) :
            if (isinstance(time_tick[i], int)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'
                
        elif (i != (ctrl_num - 1) and isCondense == False) :
            if (isinstance(time_tick[i], int)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'

    fig_e = ax.get_figure()
    if (isShow) :
        fig_e.text(0.45, -0.08, txt, ha = 'left',  bbox = dict(facecolor = 'green', alpha = 0.35))        
    fig_e.set_size_inches(16, 9, forward = True)
    if (isCondense) :
        fig_e.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_min_errorbar.png', dpi = 120, bbox_inches = "tight")
    else :
        fig_e.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_errorbar.png', dpi = 120, bbox_inches = "tight")
    plt.show()

def threshold_error_zoom(df, error, threshold, title, filepath, ctrl_num, isShow, isCondense, xmax, xmin, ymax, ymin):
    filename = os.path.splitext(filepath)[0]
    if (isCondense) :
        df = df.groupby(np.arange(len(df))//60).mean()
        error = error[error.index % 60 == 0]
        error = error.reset_index(drop = True)
        print("Data condensed")     
    ax = df.plot(yerr = error, linestyle = '-', linewidth = 0.75)
    ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
    time_tick = []

    for i in range(1, len(df.columns) + 1) :
        if (i != ctrl_num - 1) :
            green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
            colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = ".")

            if (isCondense) :
                if (len(green_list) >= 10) :
                    for i in range(2, len(green_list) - 10) :
                        if (green_list[i] + 9 == green_list[i + 9]) :
                            time_tick.append(green_list[i])
                            break
                else :
                    time_tick.append('No valid colour shift detected')
            else :
                if (len(green_list) > 600) :
                    for i in range(2, len(green_list) - 100) :
                        if (green_list[i] + 90 == green_list[i + 90]) :
                            time_tick.append(green_list[i])
                            break
                else :
                    time_tick.append('No valid colour shift detected')
    
    if (isCondense) :
        ax.set_xlabel("Time(min)")
    else :
        ax.set_xlabel("Time(sec)")

    ax.set_ylabel("Growth(dB)")
    ax.legend(title = (str)(threshold * 100) + " % threshold")
    ax.title.set_text(title)

    txt = 'Colour shift info: \n'
    for i in range (0, len(time_tick)) :
        if (i + 1 == ctrl_num) :
            txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                
        if (i != (ctrl_num - 1) and isCondense == True) :
            if (isinstance(time_tick[i], int)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'
                
        elif (i != (ctrl_num - 1) and isCondense == False) :
            if (isinstance(time_tick[i], int)) :
                if (i < len(time_tick) - 1) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i] + ' \n'

    fig = ax.get_figure()
    if (isShow):
        fig.text(0.45, -0.08, txt, ha = 'left',  bbox = dict(facecolor = 'green', alpha = 0.35))      
    fig.set_size_inches(16, 9, forward = True)
    ax_zoom = ax
    ax_zoom.set_xlim([xmin, xmax])
    ax_zoom.set_ylim([ymin, ymax])
    fig = ax_zoom.get_figure()
    if (isCondense) :
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_min_errorbar.png', dpi = 120, bbox_inches = "tight")
    else :
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_errorbar.png', dpi = 120, bbox_inches = "tight")    
    plt.show()

'''
SIMPLE STARTERS
'''
def graph(data, filepath):
    filename = os.path.splitext(filepath)[0]
    ax_sec = data.plot()
    ax_sec.set_xlabel("Time(sec)")
    ax_sec.set_ylabel("Growth(dB)")
    fig = ax_sec.get_figure()
    fig.set_size_inches(16, 9)
    fig.savefig(filename + 'sec_fig.png', dpi = 120)

    df = data.groupby(np.arange(len(data))//60).mean()
    ax = df.plot()
    fig = ax.get_figure()
    ax.set_xlabel("Time(min)")
    ax.set_ylabel("Growth(dB)")
    fig.set_size_inches(16, 9)
    fig.savefig(filename + 'min_fig.png', dpi = 120)
    plt.show()
def thresholdGraph(data, threshold, title, filepath, isShow):
    if (threshold > 1 or threshold < 0):
        print("Invalid threshold, must be a number between 0 to 1")
        return None

    else:
        filename = os.path.splitext(filepath)[0]
        
        
        df = data.groupby(np.arange(len(data))//60).mean()
        print("Data condensed")
        print(df)
        
        
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = 6, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        for i in range(2, len(df.columns) + 1):
            green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, 0] * threshold].index.tolist()
            colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, 0]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

            if (len(green_list) >= 10):
                ''' DISCUSS ACCURACY
                '''
                for i in range(2, len(green_list) - 10):
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
        if (isShow):
            fig.text(0.45, -0.05, txt, ha = 'left',  bbox = dict(facecolor = 'green', alpha = 0.4))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120, bbox_inches = "tight")
        plt.show()
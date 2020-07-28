import matplotlib.pyplot as plt
import os
import numpy as np


def threshold_final(df, threshold, title, filepath, ctrl_num, isShow, isCondense):
    filename = os.path.splitext(filepath)[0]
    
    if (isCondense) :
        df = df.groupby(np.arange(len(df))//60).mean()
        print("\nData condensed\n")
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) > 10) :
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
        
        if (ctrl_num > len(time_tick)) :
             for i in range (0, len(time_tick)) :
                if (isinstance(time_tick[i], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
             txt = txt + 'Channel ' + str(ctrl_num) + ': ' +  df.columns[ctrl_num - 1] + " (Control)"
        else:
            for i in range (0, len(time_tick) + 1) :
                if (i + 1 == ctrl_num) :
                    txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                elif (isinstance(time_tick[i - 1], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " minute\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " minute"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
                        
        fig = ax.get_figure()
        if (isShow) :
            fig.text(0.45, -0.06, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.35))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold_min.png', dpi = 120, bbox_inches = "tight")
        plt.show()
        
    else:
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) > 600) :
                    for j in range(2, len(green_list) - 100) :
                        if (green_list[j] + 60 == green_list[j + 60]) :
                            time_tick.append(green_list[j])
                            break
                else :
                    time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(sec)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
        txt = 'Colour shift info: \n'
        
        if (ctrl_num > len(time_tick)) :
             for i in range (0, len(time_tick)) :
                if (isinstance(time_tick[i], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
             txt = txt + 'Channel ' + str(ctrl_num) + ': ' +  df.columns[ctrl_num - 1] + " (Control)"
        else:
            for i in range (0, len(time_tick) + 1) :
                if (i + 1 == ctrl_num) :
                    txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                elif (isinstance(time_tick[i - 1], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " second\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " second"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
                        
        fig = ax.get_figure()
        if (isShow) :
            fig.text(0.45, -0.08, txt, ha = 'left',  bbox = dict(facecolor = 'red', alpha = 0.35))
        fig.set_size_inches(16, 9, forward = True)
        fig.savefig(filename + '_' + (str)(threshold * 100) + '%_threshold.png', dpi = 120, bbox_inches = "tight")
        plt.show()
  

def threshold_zoom(df, threshold, title, filepath, ctrl_num, isShow, isCondense, xmax, xmin, ymax, ymin):
    filename = os.path.splitext(filepath)[0]
    
    if (isCondense) :
        df = df.groupby(np.arange(len(df))//60).mean()
        print("\nData condensed\n")
        
        ax = df.plot()
        ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
        time_tick = []
        
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) > 10) :
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
        
        if (ctrl_num > len(time_tick)) :
             for i in range (0, len(time_tick)) :
                if (isinstance(time_tick[i], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
             txt = txt + 'Channel ' + str(ctrl_num) + ': ' +  df.columns[ctrl_num - 1] + " (Control)"
        else:
            for i in range (0, len(time_tick) + 1) :
                if (i + 1 == ctrl_num) :
                    txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                elif (isinstance(time_tick[i - 1], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " minute\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " minute"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
                    
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
        
        for i in range(1, len(df.columns) + 1) :
            if (i != ctrl_num) :
                green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
                colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
                ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = "|")

                if (len(green_list) > 600) :
                    for j in range(2, len(green_list) - 100) :
                        if (green_list[j] + 60 == green_list[j + 60]) :
                            time_tick.append(green_list[j])
                            break
                else :
                    time_tick.append('No valid colour shift detected')

        ax.set_xlabel("Time(sec)")
        ax.set_ylabel("Growth(dB)")
        ax.legend(title = (str)(threshold * 100) + " % threshold")
        ax.title.set_text(title)
        txt = 'Colour shift info: \n'
        
        if (ctrl_num > len(time_tick)) :
             for i in range (0, len(time_tick)) :
                if (isinstance(time_tick[i], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
             txt = txt + 'Channel ' + str(ctrl_num) + ': ' +  df.columns[ctrl_num - 1] + " (Control)"
        else:
            for i in range (0, len(time_tick) + 1) :
                if (i + 1 == ctrl_num) :
                    txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
                elif (isinstance(time_tick[i - 1], int)) :
                    if (i < len(time_tick)) :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " second\n"
                    else :
                        txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " second"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
                        
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
        print("\nData condensed\n")     
    
    ax = df.plot(yerr = error, linestyle = '-', linewidth = 0.65)
    ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
    time_tick = []
    
    for i in range(1, len(df.columns) + 1) :
        if (i != ctrl_num) :
            green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
            colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = ".")
            if (isCondense) :
                if (len(green_list) > 10) :
                    for i in range(2, len(green_list) - 10) :
                        if (green_list[i] + 9 == green_list[i + 9]) :
                            time_tick.append(green_list[i])
                            break
                else :
                    time_tick.append('No valid colour shift detected')
            else :
                if (len(green_list) > 600) :
                    for i in range(2, len(green_list) - 100) :
                        if (green_list[i] + 60 == green_list[i + 60]) :
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
    
    if (ctrl_num > len(time_tick)) :
        for i in range (0, len(time_tick)) :
           if (isinstance(time_tick[i], int) and isCondense == False) :
               if (i < len(time_tick)) :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
               else :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
           elif (isinstance(time_tick[i], int) and isCondense == True) :
               if (i < len(time_tick)) :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
               else :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
           else :
               txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
        
        txt = txt + 'Channel ' + str(ctrl_num) + ': ' +  df.columns[ctrl_num - 1] + " (Control)"
    
    else:
        for i in range (0, len(time_tick) + 1) :
            if (i + 1 == ctrl_num) :
                txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
            elif (isinstance(time_tick[i - 1], int) and isCondense == False) :
                if (i < len(time_tick)) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " second\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " second"
            elif (isinstance(time_tick[i - 1], int) and isCondense == True) :
                if (i < len(time_tick)) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " minute\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " minute"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
    
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
        print("\nData condensed\n")     
    
    ax = df.plot(yerr = error, linestyle = '-', linewidth = 0.65)
    ax_ctrl = df.reset_index().plot(x = 'index', y = ctrl_num, kind = 'scatter', ax = ax, c = "b")
    time_tick = []
    
    for i in range(1, len(df.columns) + 1) :
        if (i != ctrl_num) :
            green_list = df.iloc[:, (i - 1)][df.iloc[:, (i - 1)] < df.iloc[:, (ctrl_num - 1)] * threshold].index.tolist()
            colors = np.where(df.iloc[:, (i - 1)] > df.iloc[:, (ctrl_num - 1)]*threshold, 'r', 'g')
            ax_i = df.reset_index().plot(x = 'index', y = i, kind = 'scatter', ax = ax, c = colors, marker = ".")
            if (isCondense) :
                if (len(green_list) > 10) :
                    for i in range(2, len(green_list) - 10) :
                        if (green_list[i] + 9 == green_list[i + 9]) :
                            time_tick.append(green_list[i])
                            break
                else :
                    time_tick.append('No valid colour shift detected')
            else :
                if (len(green_list) > 600) :
                    for i in range(2, len(green_list) - 100) :
                        if (green_list[i] + 60 == green_list[i + 60]) :
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
    
    if (ctrl_num > len(time_tick)) :
        for i in range (0, len(time_tick)) :
           if (isinstance(time_tick[i], int) and isCondense == False) :
               if (i < len(time_tick)) :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " second\n"
               else :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " second"
           elif (isinstance(time_tick[i], int) and isCondense == True) :
               if (i < len(time_tick)) :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i]) + " minute\n"
               else :
                   txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i]) + " minute"
           else :
               txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'
        
        txt = txt + 'Channel ' + str(ctrl_num) + ': ' +  df.columns[ctrl_num - 1] + " (Control)"
    
    else:
        for i in range (0, len(time_tick) + 1) :
            if (i + 1 == ctrl_num) :
                txt = txt + 'Channel ' + str(i + 1) + ': ' +  df.columns[i] + " (Control)\n"
            elif (isinstance(time_tick[i - 1], int) and isCondense == False) :
                if (i < len(time_tick)) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " second\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " second"
            elif (isinstance(time_tick[i - 1], int) and isCondense == True) :
                if (i < len(time_tick)) :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' at ' + str(time_tick[i - 1]) + " minute\n"
                else :
                    txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i]  + ' at ' + str(time_tick[i - 1]) + " minute"
            else :
                txt = txt + 'Channel ' + str(i + 1) + ': '+  df.columns[i] + ' ' + time_tick[i - 1] + ' \n'

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

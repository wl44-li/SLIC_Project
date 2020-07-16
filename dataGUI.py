from tkinter import filedialog
import pygubu
import cleanData
from fileHelper import readFile
import pandas as pd
import simpleGraph
import sys

class SLIC_DataTool:
    ''' Main class
    '''

    def __init__(self):
        ''' Initilise GUI
        '''
        self.builder = builder = pygubu.Builder()
        builder.add_from_file('SLIC_ui_1.2.ui')
        self.mainwindow = builder.get_object("Data_Func")
        builder.connect_callbacks(self)

    def button1_callback(self):
        ''' Click action of the first button - Threshold graph
        '''
        num_f = self.builder.tkvariables['number_file'].get()
        num_c = self.builder.tkvariables['channel_number'].get()
        col_h = self.builder.tkvariables['col_list'].get()
        col_u = self.builder.tkvariables['col_unit'].get()
        graph_h = self.builder.tkvariables['graph_title'].get()
        threshold_p = self.builder.tkvariables['threshold'].get()
        isShow = self.builder.tkvariables['is_show'].get()
            
        col_list = [x.strip() for x in col_h.split()]
        file_list = []

        for i in range(num_f):
            filename = filedialog.askopenfilename()
            file_list.append(filename)

        if num_f == 1:
            data = readFile(file_list[0])
            if data is not None:
                data = cleanData.remove_string(col_list, num_c, col_u, data)
                print("Data refined\n")
                data = cleanData.baseline_correct(data)
                print("Data baseline corrected\n")
                cleanData.saveData(file_list[0], data)
                print("Data saved\n")
                simpleGraph.thresholdGraph(data, threshold_p/100, graph_h, file_list[0], isShow)

        else:
            df_list = [readFile(filename) for filename in file_list]
            clean_list = []
            for i in range(0, len(df_list)):
                df = cleanData.refineData(col_list, num_c, col_u, df_list[i])
                cleanData.saveData(file_list[i], df)
                clean_list.append(df)

            df_concat = pd.concat(clean_list)
            by_row_index = df_concat.groupby(df_concat.index)
            df_means = by_row_index.mean()
            print("Data collated and averaged\n")
            df_sem = by_row_index.sem()
            simpleGraph.thresholdGraph(df_means, threshold_p/100, graph_h, file_list[0], isShow)
            simpleGraph.threshold_errorbar(df_means, df_sem, threshold_p/100, graph_h, file_list[0], isShow)


    def button2_callback(self):
        ''' Click action of second button - Zoom in snapshot 
        '''
        num_f = self.builder.tkvariables['number_file'].get()
        num_c = self.builder.tkvariables['channel_number'].get()
        col_h = self.builder.tkvariables['col_list'].get()
        col_u = self.builder.tkvariables['col_unit'].get()
        graph_h = self.builder.tkvariables['graph_title'].get()
        threshold_p = self.builder.tkvariables['threshold'].get()
        x_min = self.builder.tkvariables['x_min'].get()
        x_max = self.builder.tkvariables['x_max'].get()
        y_min = self.builder.tkvariables['y_min'].get()
        y_max = self.builder.tkvariables['y_max'].get()
        isShow = self.builder.tkvariables['is_show'].get()

        col_list = [x.strip() for x in col_h.split()]
        file_list = []

        for i in range(num_f):
            filename = filedialog.askopenfilename()
            file_list.append(filename)

        if num_f == 1:
            data = readFile(file_list[0])
            if data is not None:
                data = cleanData.remove_string(col_list, num_c, col_u, data)
                data = cleanData.baseline_correct(data)
                simpleGraph.threshold_zoom(data, threshold_p/100, graph_h, file_list[0], isShow, x_max, x_min, y_max, y_min)

        else:
            df_list = [readFile(filename) for filename in file_list]
            clean_list = []
            for df in df_list:
                df = cleanData.refineData(col_list, num_c, col_u, df)
                clean_list.append(df)

            df_concat = pd.concat(clean_list)
            by_row_index = df_concat.groupby(df_concat.index)
            df_means = by_row_index.mean()
            df_sem = by_row_index.sem()
            simpleGraph.threshold_error_zoom(df_means, df_sem, threshold_p/100, graph_h, file_list[0], isShow, x_max, x_min, y_max, y_min)  
        
    def run(self):
        self.mainwindow.mainloop()  
        
    def quit_callback(self):
        ''' Click action for quit button
        '''
        self.mainwindow.destroy()
        sys.exit()
        
if __name__ == '__main__':
    app = SLIC_DataTool()
    app.run()

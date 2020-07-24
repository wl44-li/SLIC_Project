import pandas as pd
import tkinter as tk
from tkinter import filedialog
import cleanData
from fileHelper import readFile
import simpleGraph
import os

'''
Script to Perform average across 3 runs of SLIC data - Usual case
'''
# Use Tkinter to get file explorer window
root = tk.Tk()

# Hide full GUI for the time being
root.withdraw()

file_list = []

# range can be changed via GUI
for i in range(3):
    filename = filedialog.askopenfilename()
    file_list.append(filename)

# Get col_list from GUI instead
base = os.path.basename(file_list[0])
baseFile = os.path.splitext(base)[0]
channel_string = baseFile.split('(')[0]
col_list = [x.strip() for x in channel_string.split(',')]

# Populate a list of dateframe from raw data
df_list = [readFile(filename) for filename in file_list]
clean_list = []

# refine all dataframes
for df in df_list:
    df = cleanData.refineData(col_list, 6, "ug/ml", df, False)
    clean_list.append(df)

# Concate dataframes together
df_concat = pd.concat(clean_list)

by_row_index = df_concat.groupby(df_concat.index)

df_means = by_row_index.mean()

# Standard error calcualted based on mean
df_sem = by_row_index.sem()
# print(df_sem)
# generate graph from averaged data
# simpleGraph.graph(df_means, file_list[0].split('(')[0] + '_avg_')
# simpleGraph.thresholdGraph(df_means, 0.50, "Threshold Graph", file_list[0].split('(')[0] + '_avg_', True)

# option to add error bars
simpleGraph.threshold_errorbar(df_means, df_sem, 0.50, "Threshold Graph", file_list[0], 1, True, False)

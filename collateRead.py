import pandas as pd
import tkinter as tk
from tkinter import filedialog
import cleanData
from fileHelper import readFile
import simpleGraph
import os

'''
Perform average across 3 runs of SLIC data
'''

# Use Tkinter to get file explorer window
root = tk.Tk()

# Hide full GUI for the time being 
root.withdraw()

''' Could improve to a for loop based on user GUI input ?
'''
# Get the path to raw data csv file
raw_file_path_1 = filedialog.askopenfilename()

raw_file_path_2 = filedialog.askopenfilename()

raw_file_path_3 = filedialog.askopenfilename()

'''
print(raw_file_path_1)
print(raw_file_path_2)
print(raw_file_path_3)
'''

base = os.path.basename(raw_file_path_1)
baseFile = os.path.splitext(base)[0]
channel_string = baseFile.split('(')[0]
col_list = [x.strip() for x in channel_string.split(',')]
print(col_list) # Used to name column headers


df_1 = readFile(raw_file_path_1)
df_2 = readFile(raw_file_path_2)
df_3 = readFile(raw_file_path_3)


df_1 = cleanData.refineData(col_list, df_1)
print("Data 1 refined")
cleanData.saveData(raw_file_path_1, df_1)
print("Data 1 baseline corrected")

df_2 = cleanData.refineData(col_list, df_2)
print("Data 2 refined")
cleanData.saveData(raw_file_path_2, df_2)
print("Data 2 baseline corrected")

df_3 = cleanData.refineData(col_list, df_3)
print("Data 3 refined")
cleanData.saveData(raw_file_path_3, df_3)
print("Data 3 baseline corrected")

# Concate dataframes together
df_concat = pd.concat((df_1, df_2, df_3))

by_row_index = df_concat.groupby(df_concat.index)

df_means = by_row_index.mean()

'''
print(df_means)
print(raw_file_path_1.split('(')[0])
'''

# generate graph from averaged data
simpleGraph.graph(df_means, raw_file_path_1.split('(')[0] + '_avg_')
simpleGraph.thresholdGraph(df_means, 0.50, raw_file_path_1.split('(')[0] +  '_avg_')

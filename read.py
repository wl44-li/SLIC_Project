import pandas as pd
import tkinter as tk
from tkinter import filedialog
import cleanData
from fileHelper import readFile
import simpleGraph
import os
# Use Tkinter to get file explorer window
root = tk.Tk()

# Hide full GUI for the time being 
root.withdraw()

# Get the path to raw data csv file
raw_file_path = filedialog.askopenfilename()

# Extract list of column variables from filepath -> Change to Tkinter GUI later
base = os.path.basename(raw_file_path)
baseFile = os.path.splitext(base)[0]
channel_string = baseFile.split('(')[0]
col_list = [x.strip() for x in channel_string.split(',')]
print(col_list) # Used to name column headers

data = readFile(raw_file_path)

if data is not None:
    data = cleanData.refineData(col_list, data)
    print("Data refined")
    cleanData.saveData(raw_file_path, data)
    print("Data baseline corrected")
    
    # Simple seconds and minutes graph
    simpleGraph.graph(data, raw_file_path)
    
    # scatter graph based on threshold (value between 0 to 1) given via GUI
    simpleGraph.thresholdGraph(data, 0.50, raw_file_path)
    
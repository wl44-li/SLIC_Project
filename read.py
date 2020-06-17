import pandas as pd
import tkinter as tk
from tkinter import filedialog
import cleanData
from fileHelper import readFile
import simpleGraph


root = tk.Tk()

# Hide full GUI for the time being 
root.withdraw()

# Get the path to raw data
raw_file_path = filedialog.askopenfilename()

print(raw_file_path, "\n")

data = readFile(raw_file_path)

if data is not None:
    data = cleanData.refineData(data)
    print("Data refined")
    cleanData.saveData(raw_file_path, data)
    print("Data baseline corrected")
    
    # seconds and minutes graph
    simpleGraph.graph(data, raw_file_path)
    
    # scatter graph based on threshold (value between 0 to 1)
    simpleGraph.thresholdGraph(data, 0.25, raw_file_path)
import pandas as pd
import tkinter as tk
import os
from tkinter import filedialog
import cleanData
from fileHelper import fileValid, readFile

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
    

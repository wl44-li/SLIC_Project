import tkinter as tk
from tkinter import filedialog
import cleanData
import simpleGraph
from fileHelper import readFile

''' Script to Read, clean on a single raw data file
'''
# Use Tkinter to get file explorer window
root = tk.Tk()

# Hide full GUI for the time being
root.withdraw()

# Get the path to raw data csv file
raw_file_path = filedialog.askopenfilename()

col_list = [0, 2, 4, 8, 16, 32]

data = readFile(raw_file_path)

print(data)
print("raw data read in")

if data is not None:
    data = cleanData.remove_string(col_list, 6, "ug/ml", data, False)
    print("Data refined\n")
    print(data)

    data = cleanData.baseline_correct(data)
    print("Data baseline corrected\n")
    print(data)

    cleanData.saveData(raw_file_path, data)
    print("Data saved\n")
        
    simpleGraph.threshold_final(data, 0.5, "Header", raw_file_path, 1, True, True)
    
    
    
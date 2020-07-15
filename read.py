import tkinter as tk
from tkinter import filedialog
import cleanData
from fileHelper import readFile

''' Script to Read, clean on a single raw data file
'''
# Use Tkinter to get file explorer window
root = tk.Tk()

# Hide full GUI for the time being
root.withdraw()

# Get the path to raw data csv file
raw_file_path = filedialog.askopenfilename()

col_list = [0, 1, 2, 3, 4, 5]

data = readFile(raw_file_path)

if data is not None:
    data = cleanData.remove_string(col_list, 6, "ug/ml", data)
    print("Data refined\n")

    data = cleanData.baseline_correct(data)
    print("Data baseline corrected\n")

    cleanData.saveData(raw_file_path, data)
    print("Data saved\n")
    
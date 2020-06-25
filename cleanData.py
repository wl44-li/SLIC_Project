import sys
import pandas as pd
import os
from fileHelper import *

def clean(filepath):
    """Runs independently to check data, refine data and save data to a new clean .tsv file"""
    data = readFile(filepath)
    if data is not None:
        data = refineData(data)
        saveData(filepath, data)

# ask save directory from user
def saveData(filepath, data):
    """
    Saves pre-processed data to a new csv file in the same directory
    """
    filename = os.path.splitext(filepath)[0]
    data.to_csv(filename + "_clean.csv", index = False)
    

def refineData(col_list, data):
    """
    First remove extra string
    Then perform baseline correction
    """
    data = remove_string(col_list, data)
    data = baseline_correct(data)
    return data    


def remove_string(col_list, df):
    """
    Remove all alphabets
    Expand to 6 channels
    Remove useless channels
    Drop entries with fewer than 6 channels
    Remove first 3 rows
    Rename column headers
    Reset index
    """
    
    start_list = df[0][df[0] == 'OK System running'].index.tolist()
    
    # Only keep last system start run
    if len(start_list) > 1:
        print("Warning: More than one 'System start' detected")
        # remove error system starts
        df = df.iloc[start_list[len(start_list) - 1]:]
        print(start_list[len(start_list) - 1], "rows have been removed from start\n")
        
    # remove all alphabets
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(r"[a-zA-Z]", '')
    df.iloc[:, 0] = df.iloc[:, 0].str.replace("#", '')

    # split into channels by space
    df = df[0].str.split(expand = True)

    # Intepretate 6 channels (This may increase to 16 - modified via GUI)   
    while (len(df.columns) > 6):
        # delete redundant columns (last 2 for example) --- Works on Version 7 of SLICS
        df.drop(df.columns[-1], axis = 1, inplace = True)
        
    # remove entry with less than 6 channels of data
    df = df[df[5].notna()]

    # remove the first three rows from "warmming up" SLIC - Customisable via GUI
    df = df.iloc[3:]
    
    # unit should be customisable via GUI
    unit = "ug/ml"
    
    # rename header (Currently at 6 channels, first being the control)
    df.columns = ['Control', 'Channel 1: ' + col_list[1] + unit, 'Channel 2: ' + col_list[2] + unit, 'Channel 3: ' + col_list[3] + unit, 'Channel 4: ' + col_list[4] + unit, 'Channel 5: ' + col_list[5] + unit]
    
    # reset index
    df = df.reset_index(drop = True)
    return df

def baseline_correct(df):
    """
    Substract first row from all rows
    """
    # treat all columns as numeric values
    df = df.apply(pd.to_numeric)
    
    # substract first row from all other rows
    df = df - df.iloc[0]
    return df
    
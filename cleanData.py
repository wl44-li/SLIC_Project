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


def saveData(filepath, data):
    """
    Saves pre-processed data to a new csv file in the same directory
    """
    filename = os.path.splitext(filepath)[0]

    data.to_csv(filename + "_clean.csv", index = False)
    

def refineData(data):
    """
    First remove extra string
    Then perform baseline correction
    """
    data = remove_string(data)
    data = baseline_correct(data)
    return data    

# add another parameter to represent number of useful channels ?
def remove_string(df):
    # remove stop in last entry
    df.iloc[-1] = df.iloc[-1].str.replace("stop ", "")
    
    # split into channels
    df = df[0].str.split(expand = True)

    # Intepretate 6 channels (This may increase to 16)   
    while (len(df.columns) > 6):
        # delete redundant columns 
        df.drop(df.columns[-1], axis = 1, inplace = True)
        
    # remove entry with less than 2 channels of data
    df = df[df[1].notna()]
    
    # remove the first three rows from "warmming up" SLIC
    df = df.iloc[3:]
    
    # rename header (Currently at 6 channels, first being the control)
    df.columns = ['Control', 'Channel 1', 'Channel 2', 'Channel 3', 'Channel 4', 'Channel 5']
    
    # reset index
    df = df.reset_index(drop=True)
    return df

def baseline_correct(df):
    # treat all columns as numeric values
    df = df.apply(pd.to_numeric)
    
    # substract first row from all other rows
    df = df - df.iloc[0]
    return df
    
import pandas as pd
import os
from fileHelper import *

def clean(filepath):
    """Functions to check data, refine data and save data to a new clean .tsv file"""
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


def refineData(col_list, num, col_unit, data):
    """
    First remove extra string
    Then perform baseline correction
    """
    data = remove_string(col_list, num, col_unit, data)
    data = baseline_correct(data)
    return data


def remove_string(col_list, col_num, col_unit, df):
    """
    Remove extra 'System running' as noise
    Remove all alphabets
    Expand to 6 OR more channels (up to 64)
    Remove useless channels
    Drop entries with fewer than 6 channels
    Remove first 3 rows (warmming up SLIC)
    Rename column headers
    Reset index
    """

    start_list = df[0][df[0] == 'OK System running'].index.tolist()

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

    # Intepretate 6 channels
    while (len(df.columns) > col_num):
        # delete redundant columns (last 2 for example) --- Works on Version 7 of SLIC data
        df.drop(df.columns[-1], axis = 1, inplace = True)

    # remove entry with less than 6 channels of data
    df = df[df[5].notna()]

    # remove the first three rows from "warmming up" SLIC - Customisable via GUI
    df = df.iloc[3:]

    # rename header (Currently at 6 channels, first being the control)
    list_c = []

    for i in range (col_num):
         list_c.append(col_list[i] +  ' ' + col_unit)

    df.columns = list_c
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

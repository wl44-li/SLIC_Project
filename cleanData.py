import pandas as pd
import os
from fileHelper import *
import re

def saveData(filepath, data):
    ''' Save data to new csv file
    Parameters
    ----------
    filepath : directory of original raw data
    data : data to be saved
    '''
    filename = os.path.splitext(filepath)[0]
    data.to_csv(filename + "_clean.csv", index = False)


def refineData(col_list, num, col_unit, data):
    ''' Remove string + baseline correct
    
    Parameters
    ----------
    col_list : data of channels
    num : number of channels
    col_unit : unit of channels
    data : raw dataframe

    Returns
    -------
    data : cleaned and baseline corrected
        dataframe.

    '''
    data = remove_string(col_list, num, col_unit, data)
    data = baseline_correct(data)
    return data

def extract(string):
    ''' Extra cleanning function to deal with negative entries

    Parameters
    ----------
    string : string to clean

    Returns
    -------
    string without any number, - or . in front
    '''
    return re.sub('^\d*\.*\^*-+', '-', string)
    
def remove_string(col_list, col_num, col_unit, df):
    ''' Support version 7 of SLIC
    
    Remove extra 'System running' as noise
    Remove all alphabets
    Expand to 6 OR more channels (up to 64)
    Remove useless channels
    Drop entries with fewer than 6 channels
    Remove first 3 rows (warmming up SLIC)
    Rename column headers
    Reset index

    Parameters
    ----------
    col_list : list of column entries.
    col_num : number of channels.
    col_unit : unit of channel.
    df : raw dataframe.

    Returns
    -------
    df : cleaned dataframe.
    '''
    start_list = df[0][df[0] == 'OK System running'].index.tolist()

    if len(start_list) > 1:
        print("Warning: More than one 'System start' detected")
        # remove error system startsp
        df = df.iloc[start_list[len(start_list) - 1]:]
        print(start_list[len(start_list) - 1], "rows have been removed from start\n")
          
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(r"[a-zA-Z]", '')
    df.iloc[:, 0] = df.iloc[:, 0].str.replace(r"[^\w\s^.^-]|_", '')
    df.iloc[:, 0] = df.iloc[:, 0].apply(extract)
    df = df[0].str.split(expand = True)
    
    while (len(df.columns) > col_num):
        df.drop(df.columns[-1], axis = 1, inplace = True)

    df = df[df[col_num - 1].notna()]
    df = df.iloc[3:]
    list_c = []

    for i in range (col_num):
         list_c.append(str(col_list[i]) + ' ' + col_unit.strip())
         
    df.columns = list_c
    df = df.reset_index(drop = True)
    return df

def baseline_correct(df):
    ''' Perform baseline correction

    Parameters
    ----------
    df : dataframe

    Returns
    -------
    df : dataframe
    '''

    df = df.apply(pd.to_numeric)
    df = df - df.iloc[0]
    return df

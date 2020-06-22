import os
import pandas as pd

def fileValid(filepath):
    """
    Checks if a file is a valid file according to the oc library
    """
    valid = os.access(filepath, os.R_OK)
    return valid

def readFile(filepath):
    """
    Opens a file as a pandas dataframe and checks if it is a valid file.
    Returns either the dataframe or None.
    """
    if fileValid(filepath) :
        print("Reading From: " + filepath)
        
        # read noisy string as NaN, drop before processing further
        data = pd.read_csv(filepath, header = None, sep = '\r\t', 
               na_values = ['OK System stopped', 'OK System running', 'start 1', 'start v1', 'stop', 'p', 'op', 'top'], 
               engine = 'python').dropna()
        
        # 'htr md 0' & 'OK mode set' or 'ERR ...'
        return data
    
    else:
        print("File Unable To Be Read")
        return None


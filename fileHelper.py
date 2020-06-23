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
        
        data = pd.read_csv(filepath, header = None, sep = '\r\t', engine = 'python')
        
        return data
    
    else:
        print("File Unable To Be Read")
        return None


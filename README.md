# SLIC_Project
# Author : Weiye Li (wl44)

Working on intepretating data obtained via SLIC, with a flexible GUI

1. Find Spyder from Windows start Menu

2. Open 'dataGUI.py' in Spyder

3. Run 'dataGUI.py' in Spyder

4. Follow Interface to generate graphs, use Spyder to navigate view

    4.1 Information filling guidance:
    
         Number of File: Must be a integer value greater than 1. NOTE, if working on a single file, no error bar graph will be generated
         
         Channel Unit: the unit used to measure experimental chemical (i.e ug/ml, mg/ml)
         
         Channel Data: the value of each SLIC channel separated by space, i.e. ( 0 2 4 8 16 32) NOTE, value must be distinct!
         
         Ctrl Channel Index: an index from 1 to the number of channels denoting control channel position. 
                             i.e. if control is on the left, its position will be 1; if on the right, its position will be 6 (given a total of 6 channels)  
    
         Graph title: the title you would add to generated graphs
         
         Threshold: a scroll bar between 0 to 100% 
         
         Show colour shift analysis: check the box if you want to see a box of colour shift information at the bottom of graphs
         
         Show condensed graph: check the box if you want to graph over minute rather than second
         
         Run with previous SLIC: CAUTIOUs, DO NOT check the box if running with current SLIC (7.1)
    
5. Generated graphs and cleaned raw data are saved in the same directory as supplied raw data

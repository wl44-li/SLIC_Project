# SLIC_Data_Tool_Project_2020_Summer
# Author : Weiye Li (wl44@st-andrews.ac.uk)
# Supervisors : Robert Hammond (rjhh), Thomas Powell (thp2)

Working on intepretating data obtained from SLIC, with a flexible GUI to generate graphs. 

User manual : 
1. Find and run Spyder from Windows start Menu

2. Open 'dataGUI.py' in Spyder

3. Run 'dataGUI.py' in Spyder

4. Follow Interface to generate graphs, use Spyder to navigate view

    4.1 GUI usage guidance:
    
         Number of File: Must be a integer value greater than 1. 
                         NOTE, if working on a single file, no error bar graph will be generated.
         
         Channel Unit: the unit used to measure experimental chemicals (i.e ug/ml, mg/ml)
         
         Channel Data: the value of each SLIC channel separated by space, i.e. ( 0 2 4 8 16 32 ) 
                       NOTE, value must be DISTINCT (no repeats). 
         
         Ctrl Channel Index: an index denoting control channel position. 
                             i.e. if control is on the left, the position will be 1; if on the right, its position will be 6 (given 6 channels in total)
    
         Graph title: the title you would add to the generated graphs
         
         Threshold: a scroll bar between 0 to 100%
         
         Show colour shift analysis: check the box if you want to see a box of colour shift information at the bottom of graphs
                                     Note, earliest minute shift is at 2 minutes; earliest second shift is at 120 seconds.
         
         Show condensed graph: check the box if you want to condense graph over minute rather than second on x-axis
         
         Run with previous SLIC: CAUTIOUS, DO NOT check the box if you are running with current SLIC (Ver 7.1)
         
         Zoom-In Snapshot fields: you can leave xmax, xmin, ymax, ymin unfilled, unless you would like to generate a 
                                  zoomed-in shot of the graph from the main configuration.
    
5. Generated graphs and cleaned raw data are saved in the same directory as supplied raw data

    5.1 Spyder also provides preview of graphs on the top right console
    
    5.2 You will probably see Spyder print out some other useful information on bottom right console, too. 
        if a run is successful, you should see "--- Success! ---" being printed after generate graph is saved. 
        
    5.3 In case of runtime failure, please copy Spyder console report and send to wl44@st-andrews.ac.uk, along with raw data if possible.    


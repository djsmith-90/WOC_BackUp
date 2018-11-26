# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 09:06:02 2018

@author: ds16565
"""

### Code to move updated release files in R:\Data\Current to their correct location in the R:\Studies\...\researchdata folder

## To do this we need a csv lookup file which lists all the R\Data\Current locations and all the R\Studies\...\researchdata locations
## to copy the files to

## First I will make a csv file with a list of all the files in R\Data\Current and their location in this folder - Then I will
## manually link this to the location in R\Studies\...\researchdata - Then I will copy the files over (using a separate .py file - 
## "movingReleaseFiles.py")

import os
import sys
import csv


################################################################
## Making a csv file with each file's location in R\Data\Current

# This syntax loops through lots of different folders within a single directory and
# exports both the file name and the file path to a CSV file

## Now make a lookup of the actual R\Data\Current directory (will save a copy as 'lookup_actual.csv')

source_dir=r'R:\Data\Current'

# Check source dir exists
if (os.path.exists(source_dir) != True):
    sys.exit('Error - Source directory does not exist! Exiting now. source_dir='+source_dir)

# Make sure source directory is correct
print ('Source directory is: '+source_dir)

fileName = [] # Make an empty list to fill with files
folder = [] # Make an empty list to fill with directory names
    
#Loop through all folders, subfolders and files
for subdir, dirs, files in os.walk(source_dir):
    
    # Loop over all files in the directory
    for fil in files: 
        
        # Specify files which end in .sav or .dta (SPSS or Stata files) 
        if fil.endswith(".sav") or fil.endswith(".dta"): 
             
            # Append file name to the list 'dxa' - Also append file path to list 'folder'
            fileName.append(fil) 
            folder.append(subdir) 

# Run some prints to make sure the syntax works (i.e., number of cases)
print ('The number of files is: '+str(len(fileName)))

# Write a csv file to import the file names in to (make sure to manually change the name of this file afterwards, so
# that any changes - i.e., adding the researchdata folder locations - are not overwritten!!)
with open(r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\lookup.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    
    # Write var names as first row od csv file
    filewriter.writerow(['fileName', 'rDataFilePath'])
    
    # Now cycle through each file, adding the file name to the csv file
    for i in range(len(fileName)):
        print ('On file number '+str(i+1)+'/'+str(len(fileName)))
        filewriter.writerow([fileName[i], folder[i]])


#############################################################
## Now manually add the R\Studies\...\researchdata file paths


#############################################################
## Also want to add a lookup to copy the syntax files from working area to R\Studies\...\syntax

## Point the source directory to the folder containing the individual syntax files

source_dir=r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\syntaxFiles\IndivFiles'

# Check source dir exists
if (os.path.exists(source_dir) != True):
    sys.exit('Error - Source directory does not exist! Exiting now. source_dir='+source_dir)

# Make sure source directory is correct
print ('Source directory is: '+source_dir)

fileName = [] # Make an empty list to fill with files
folder = [] # Make an empty list to fill with directory names
    
#Loop through all folders, subfolders and files
for subdir, dirs, files in os.walk(source_dir):
    
    # Loop over all files in the directory
    for fil in files: 
        
        # Specify files which end in .sps (SPSS syntax files files) 
        if fil.endswith(".sps"): 
             
            # Append file name to the list 'dxa' - Also append file path to list 'folder'
            fileName.append(fil) 
            folder.append(subdir) 

# Run some prints to make sure the syntax works (i.e., number of cases)
print ('The number of files is: '+str(len(fileName)))

# Write a csv file to import the file names in to (make sure to manually change the name of this file afterwards, so
# that any changes - i.e., adding the researchdata folder locations - are not overwritten!!)
with open(r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\syntaxLookup.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    
    # Write var names as first row od csv file
    filewriter.writerow(['fileName', 'rDataFilePath'])
    
    # Now cycle through each file, adding the file name to the csv file
    for i in range(len(fileName)):
        print ('On file number '+str(i+1)+'/'+str(len(fileName)))
        filewriter.writerow([fileName[i], folder[i]])


#############################################################
## Now manually add the R\Studies\...\syntax file paths



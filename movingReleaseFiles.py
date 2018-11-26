# -*- coding: utf-8 -*-
"""
Created on Wed Nov 1 11:00:59 2018

@author: ds16565
"""

### Code to move updated release files in R:\Data\Current to their correct location in the R:\Studies\...\researchdata folder

## To do this we need a csv lookup file which lists all the R\Data\Current locations and all the R\Studies\...\researchdata locations
## to copy the files to

## First I will make a csv file with a list of all the files in R\Data\Current and their location in this folder (this is the
## "makingLookup.py" file) - Then I will manually link this to the location in R\Studies\...\researchdata - Then I will copy the 
## files over (this file)

import os
import sys
import csv
import shutil


#####################################################################
## Copy the files over from R\Data to R\Studies\...\research data

## Will do a test first in my 'OpalTest' working folder - Seems to work fine, so crack on with actual moving

## When running the actual moving from R\Data\Current to R\Studies\...\release data, for some reason the SPSS cct file
## kept mentioning a 'permission error', so have taken this out of the 'lookup_actual.csv' file

# Point to the file containing the look-up from the R:\Data\Current directory to R:\Studies\...\research data
csv_filepath = r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\lookup_actual.csv'

# Open this csv file and print each row
with open(csv_filepath) as fileObject:
    csv_reader = csv.reader(fileObject)

    for row in csv_reader:
        if csv_reader.line_num == 1: # Skip the first row (if is a header)
            print ("This is row 1")
            print ("")
        else: # Split each row into 3 parts
            fileName = row[0]
            rDataLocation = row[1]
            rStudiesLocation = row[2]

            # Make sure the rData file exists - Use 'os.path.join' to join the path path components together
            if (os.path.exists(os.path.join(rDataLocation, fileName)) != True):
                sys.exit('Error - Source file in R\Data does not exist! Exiting now. rDataLocation='+rDataLocation)

            # Make sure destination file exists
            if (os.path.exists(rStudiesLocation) != True):
                sys.exit('Error - destination directory in R\Studies does not exist! Exiting now. rStudiesLocation='+rStudiesLocation)

            # Copy file from R\Data directory to R\Studies directory
            print ("File " + fileName + " is moving from " + rDataLocation + " to " + rStudiesLocation)
            print ("")
            shutil.copy(os.path.join(rDataLocation, fileName), rStudiesLocation)








This folder is for testing the SPSS python script that Sam Story put together to loop through all of the R:\Data\Current directory
and add a '-9999' value label (meaning 'consent withdrawn') to all numeric variables. This script also adds a new 'aln_qlet' string
variable for child-based data (as this is necessary for integration with Opal).

Description of each file:

Generate Syntax Scripts.sps
This is an adapted version of the file Sam made and does what it says above (makes an SPSS script file for each SPSS (.sav) file in
R\Data\Current to add a value label of -9999 (consent withdrawn) and make an 'aln_qlet' variable (if QLET exists) - I have also changed
this script so that it also exports the updated SPSS file as a Stata (.dta) file as well. This script creates a 'master.sps' file from 
which all the individual script files can be run from.

makingLookup.py
This is a python script which loops through all subdirectories it's pointed at (here, R\Data\Current), finds all .sav and .dta files, 
and exports a csv file containing both the file name and the path name (as 'lookup.csv' - This file then needs to be manually updated 
with the location of the 'R\Studies\...\release data' folder that the updated SPSS and Stata files in R\Data\Current need to be copied 
to).

This file also creates a 'syntaxLookup.csv' file with the name and location of all the SPSS syntax files (here, from R:\CTeam\RCteam\
Users\DanSmith\OpalTest\syntaxFiles\IndivFiles). This file then needs to be manually updates with the location of the 'R\Studies\...\
syntax' folder that the update syntax needs to be copied to.

lookup_actual.csv
This is the final 'lookup.csv' file with all the R\Studies\...\release data path names entered as the third column.

movingReleaseFiles.py
This is a python script which reads in the lookup file and copies the updated SPSS and Stata files from their location in R\Data\Current
to the correct location in R\Studies\...\release data.

lookup_test.csv
This was a test lookup file to make sure the 'movingReleaseFiles.py' script worked - Here, the destination directory was a directory in 
the working area, rather than the actual R\Studies\...\release data location.

syntaxLookup_actual.csv
This is the final 'syntaxLookup.csv' file with all the R\Studies\...\syntax path names entered as the third column.

movingSyntaxFiles.py
This is a python script which reads in the syntaxLookup file and copies the SPSS syntax file from their current location to the correct 
location in R\Studies\...\syntax

syntaxLookup_test.csv
This was a test syntaxLookup file to make sure the 'movingSyntaxFiles.py' script worked - Here, the destination directory was a directory
in the working area, rather than the actual R\Studies\...\syntax location.

Dan Smith
23/11/2018

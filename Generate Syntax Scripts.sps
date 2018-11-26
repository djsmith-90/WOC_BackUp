* Encoding: windows-1252.

** This script contains three Python functions:.
*main(): Loop through all files in a directory, calling the function createSPSSSyntax and createSyntaxFile. A Master Syntax file is also created. 
*createSPSSSyntax(): This function can be modified to generate any SPSS syntax.
*createSyntaxFile(): This function saves the syntax for each file as a .sps file.  
** Save the file to an alternative folder structure (this empty folder structure must match the original directory structure).

** Note that aln in the OC file has missing flags, this will prevent the file from importing into Opal. We should standardise across all files. This can either be adding in the missing flag and category labels or 
removing them. - DS UPDATE: This issue has now been resolved and missing ALN flags in the OC file have been removed **

begin program.
import spss
import os # Required to "walk" through folder structure

def main():
    # Use r'file path' to ensure \ are not converted to special characters 
    rootFolder = r'R:\Data\Current' # DS - Have changed this from OpalTest working folder to actual R\Data\Current
    saveFolder = r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\syntaxFiles' # Have changed this from 'R_Current_output' to 'syntaxFiles'
    saveFolderIndivFiles = r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\syntaxFiles\IndivFiles' # DS - This is where we want to save all the syntax files (i.e., in one directory)
    masterSyntaxFilePath = r'R:\CTeam\RCteam\Users\DanSmith\OpalTest\syntaxFiles\Master.sps' # Have changed this from 'R_Current_output' to 'syntaxFiles'
    masterSyntax = ""

    overWriteSyntaxFiles = True # Set to True if you are sure it is safe to overwrite Syntax Files in the saveFolders - DS: Have set this to true while testing

    #Loop through all folders, subfolders and files
    for subdir, dirs, files in os.walk(rootFolder):
        #For all files in each sub folder    
        for file in files:
            if file.endswith(".sav"): # DS - Is one file (TD) which ends '.SAV' (not '.sav'), so have just updated manually in R\Data\Current - Or could have dnoe 'if file.lower().endswith(".sav")
    
                # DS - In the final version we don't want to save the updated version of the release file in a different place, so the filePath and saveFilePath ought to be the
                # same (i.e., take a file from R\Data\Current, make the changes, then save te file in the same location) - I have updated that here
                filePath = subdir + os.sep + str(file)
                saveFilePath = filePath

                # DS - We don't really want the .sps files to be made in the R\Data\Current folder - Much better they all go to a different location - Have updated that here
                syntaxFilePath = saveFolderIndivFiles + os.sep + file[:-4] + "_WOCupdate.sps" # DS - Have added a '_WOCupdate' text here to make the file name more obvious
                
                SPSSSyntax = createSPSSSyntax(filePath,saveFilePath)

#Uncomment the print statement to display it in the SPSS output screen                
#                print SPSSSyntax

                if createSyntaxFile(SPSSSyntax, syntaxFilePath, overWriteSyntaxFiles): 
                    masterSyntax += 'INSERT file = "' + syntaxFilePath + '".'  + os.linesep
                else:
                    print "Error creating syntax file: " + syntaxFilePath

    if createSyntaxFile(masterSyntax, masterSyntaxFilePath, True): 
        print "Master Syntax File Create: " +  masterSyntaxFilePath
    else: 
        print "Error creating Master Syntax File in '" + masterSyntaxFilePath + "'. File may already exist."
    
def createSPSSSyntax(filePath, saveFilePath):
    #This is the custom code that can be replaced with any new functionality
    #  Loop through all variables in the files and add category -9999 withdrawn. If the qlet variable exists create a aln_qlet variable
    script = ""
    excluded_variables = ['aln','qlet'] #Any variable to skip when adding -9999 can be added here in lower case

    if filePath.endswith(".sav"): 

        #Script opening the file
        script += 'Get File="' + filePath + '".' + os.linesep
        script += 'EXECUTE.' + os.linesep

        #Now actually Open the file
        spss.Submit('Get File="' + filePath + '"')
        spss.Submit('EXECUTE')

        #Assume the qlet and aln_qlet variables does not exist
        QletExists = False
        Aln_qletExists = False

        for ind in range(spss.GetVariableCount()): #Loop through variable indices
            varName = spss.GetVariableName(ind)
            
            if varName.lower() == 'qlet':
                QletExists = True
            elif varName.lower() == 'aln_qlet':
                Aln_qletExists = True
            #If the variable isn't in the excluded list then add the value label
            elif not (varName.lower() in excluded_variables):
                script += 'ADD VALUE LABELS ' + varName + ' -9999 "Consent withdrawn".' + os.linesep
        
        if QletExists and not Aln_qletExists:
                script += 'STRING aln_qlet (A15).' + os.linesep
                script += 'ADD FILES file */keep aln_qlet all.' + os.linesep
                script += 'COMPUTE aln_qlet=CONCAT(LTRIM(STRING(aln,F8)), "_", qlet).' + os.linesep
                script += 'SORT CASES BY aln_qlet(A).' + os.linesep

        script += 'EXECUTE.' + os.linesep

        #Save the file 
        script += 'SAVE OUTFILE "' + saveFilePath + '".' + os.linesep
        script += 'EXECUTE.' + os.linesep

        #DS - Save as STATA file
        script += 'SAVE TRANSLATE OUTFILE="' + saveFilePath[:-4] + '.dta"' + os.linesep
        script += '/TYPE=STATA' + os.linesep
        script += '/VERSION=13' + os.linesep
        script += '/EDITION=SE' + os.linesep
        script += '/MAP' + os.linesep
        script += '/REPLACE.' + os.linesep


    return script

def createSyntaxFile(syntaxScript, syntaxFilePath, overWriteSyntaxFiles=False):
    
    if os.path.isfile(syntaxFilePath) and overWriteSyntaxFiles==False:
        #File already exists so don't do anything and return false
        return False
    else:
        try: 
            with open(syntaxFilePath, 'w') as syntaxFile:
                syntaxFile.write(syntaxScript)
            return True
        except Exception as e:
            print(e)
            return False                    

#call the main() function to start the program
main()

end program.



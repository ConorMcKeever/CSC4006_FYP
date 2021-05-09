import sys, getopt
import pathlib
import os
import glob
import re
from convert import convertPdf
from references import getReferences
from extract import searchCitation, countCitation
from tokenizer import tokenize
from initModel import runAnalysis,initModel, initModelMovie

def main(argv):
    #Take users source and outut folders
   inputfolder = ''
   outputfolder = ''
   try:
      opts, args = getopt.getopt(argv,"hi:o:",["ifolder=","ofolder="])
   except getopt.GetoptError:
      print('app.py -i <inputfolder> -o <outputfolder>')
      sys.exit(2)
   for opt, arg in opts:
       if opt == '-h':
            print ('app.py -i <inputfolder> -o <outputfolder>')
            sys.exit()
       elif opt in ("-i", "--ifolder"):
            inputfolder = arg
       elif opt in ("-o", "--ofolder"):
            outputfolder = arg
   print('Input folder is ', inputfolder)
   print('Output folder is ', outputfolder)


   #Begin converting the source folder to the output folder
   print("Converting Files...")
   filePDF = pathlib.Path(inputfolder).glob("*.pdf")
   for file in filePDF:
       base=os.path.basename(file)
       print('Converting file: ' + os.path.splitext(base)[0])
       convertPdf(os.path.splitext(base)[0], outputfolder)
   print("Successfully converted files.\n")

   print("Training/Testing Model...")
   model = initModel()
   print("Model Ready.\n")

   #Find the reference number of the reference
   print("Searching for reference using: 'Software Errors and Complexity'" )
   countRef = 0
   py = pathlib.Path(outputfolder).glob("*.txt")

   totalRef = 0
   fileFault = 0
   posTotal = 0
   negTotal = 0
   neuTotal = 0
   for file in py:
       print("===========BEGIN NEW SEARCH===========")
       totalRef = 1 + totalRef

       print('Searching in: \'' + str(os.path.basename(file)) + '\'')
       ref = getReferences(str(file), 'Software Errors and Complexity')
       print('Reference number is : ' + str(ref) +'\n')
       if ref == 0:
           print("No references found")
           fileFault = fileFault + 1
       else:
           #Begin searching txt files for occurances of the reference
           print('Begin extracting sentences containing reference...')
           refs = countCitation(str(file), str(ref))
           if refs > 0:
               print("Extraction found " + str(refs) + " occurance(s) of reference")
               nResult,pResult = searchCitation(str(file), str(ref), model)
               fileResult = calculateAnalysis(nResult,pResult,refs)
               if  fileResult == 1:
                   posTotal = posTotal + 1
               elif fileResult == -1:
                   negTotal = negTotal + 1
               else:
                   neuTotal = neuTotal + 1
           else:
               print("No in-text references found")
       print("===========END SEARCH===========\n\n")


    #Compile data for reference to csv
   print("Total files proccessed: " + str(totalRef))
   print("Sample found " + str(posTotal) + " Positive files, " + str(neuTotal) + " Neutral Files and " + str(negTotal) + " Negative files in Total")
   print(str(fileFault) + " Files Not Proccessed")


def calculateAnalysis(neg, pos, count):
    if count != 0:
      posPercent = pos/count
      negPercent = neg/count
    if posPercent == negPercent:
        print("File is neutral")
        return 0
    else:
        print("File is "+ str(posPercent) + "% Positive")
        print("File is "+ str(negPercent) + "% Negative")
        if posPercent>negPercent:
            return 1
        else:
            return -1





if __name__ == "__main__":
    main(sys.argv[1:])

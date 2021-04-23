import sys, getopt
import pathlib
import os
import glob
import re
from convert import convert_pdf_to_txt
from references import getReferences
from extract import extractCitation
from tokenizer import tokenize

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
   print('Input folder is "', inputfolder)
   print('Output folder is "', outputfolder)


   #Begin converting the source folder to the output folder
   print("Converting Files...")
   filePDF = pathlib.Path(inputfolder).glob("*.pdf")
   for file in filePDF:
       base=os.path.basename(file)
       print('Converting file: ' + os.path.splitext(base)[0])
       convert_pdf_to_txt(os.path.splitext(base)[0], outputfolder)
   print("Successfully converted files.\n")

   #Find the reference number of the reference
   print("Searching for reference using: 'Software Errors and Complexity'" )
   countRef = 0
   py = pathlib.Path(outputfolder).glob("*.txt")
   for file in py:
       print("===========BEGIN NEW SEARCH===========")
       print('Searching in: \'' + str(os.path.basename(file)) + '\'')
       ref = getReferences(str(file), 'Software Errors and Complexity')
       print('Reference number is : ' + str(ref) +'\n')
       print('Begin extracting sentences containing reference...')

       if ref > 0:
           print(extractCitation(str(file), str(ref)))

       print("===========END SEARCH===========\n\n")
       tokenize()





if __name__ == "__main__":
    main(sys.argv[1:])

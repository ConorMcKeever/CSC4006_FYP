from extract import extractSentence
from convert import convert_pdf_to_txt
from references import getReferences
from refextract import extract_references_from_file
import pdfminer
import csv
import glob
import pathlib
import os

chFile = " "


# Menu List
menu1 = True
while menu1 == True:
    print("Citation Analysis Main Menu")
    print("1: Extract PDF to Text")
    print("2: View Extracted Files")
    print("3: Exit")
    o1 = int(input('\nChoose an option:\n'))
    if o1 == 1:
        print("This will extract from every PDF in folder then delete the PDF")
        print("Convert Files?")
        conv = input('(Y/N)\n')
        print("Converting Files...")
        filePDF = pathlib.Path('pdf').glob("*.pdf")
        for file in filePDF:
            base=os.path.basename(file)
            print('Converting file: ' + os.path.splitext(base)[0])
            convert_pdf_to_txt(os.path.splitext(base)[0])
        print("Successfully converted files.")
        print("Deleting files...")
        for file in filePDF:
            os.remove(file)
        print("Successfully deleted files in folder.")
    if o1 == 2:
        print("\nFiles in directory 'sample':")
        listNo = int(1)
        py = pathlib.Path('sample').glob("*.txt")
        for file in py:
            print('- ' + str(listNo) + '. \'' + str(os.path.basename(file)) + '\'')
            listNo += 1
        #Menu list 2
        print("*: Enter number of file you wish to edit")
        print("0: Go back to previous menu")
        o2 = int(input('\nChoose an option:\n'))
        if o2 == 0:
            menu1 = True
        else:
            listNo2 = int(1)
            py2 = pathlib.Path('sample').glob("*.txt")
            for file in py2:
                if listNo2 == o2:
                    chFile = os.path.basename(file)
                listNo2 += 1
            menu1 = False

print("You have choosen: " + chFile)

menu2 = True
while menu2 == True:
    print("\n1: Print list of references")
    print("2: Count Occurances of references")
    print("3: Extract citations to file")
    print("4: Perform citation analysis on a reference")
    print("5: Exit to Previous Menu")

    o3 = int(input('Choose an option:'))

    if o3 == 1:
        getReferences(chFile)

    if o3 == 2:
        in1 = '[' + str(input('Which reference to count:')) + ']'
        f = open('sample/' + chFile, "r")
        data = f.read()
        print("Reference [" + str(in1) + "] occurs " + str(data.count(in1) - 1) + "time(s)")
        f.close()

    if o3 == 3:
        in1 = '[' + str(input('Which reference to extract citations:')) + ']'
        print(extractSentence(chFile, in1))

    if o3 == 4:
        print('Analysis should be performed here')

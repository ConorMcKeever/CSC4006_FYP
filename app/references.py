from refextract import extract_references_from_file
import pdfminer
import csv

def getReferences(path):
    references = extract_references_from_file('sample/' + path)
    for reference in references:
        print(reference)

from refextract import extract_references_from_file
import pdfminer
import csv



references = extract_references_from_file('Core elements in the process of citing publications.pdf')


text = extract_text('Core elements in the process of citing publications.pdf')

print(references[0])


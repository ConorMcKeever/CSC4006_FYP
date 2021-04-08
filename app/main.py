from extract import extractApple
from convert import getPDFText


print("Citation Analysis Main Menu")
print("1: Print list of references")
print("2: Count Occurances of references")
print("3: Extract citations to file")
print("4: Perform citation analysis on a reference")
print("5: Extract text from PDF")

o1 = int(input('Choose an option:'))

if o1 == 5:
    getPDFText('CCRO Citation’s Context & Reasons Ontology (1).pdf')

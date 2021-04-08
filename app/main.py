from extract import extractApple
from convert import convert_pdf_to_txt


print("Citation Analysis Main Menu")
print("1: Print list of references")
print("2: Count Occurances of references")
print("3: Extract citations to file")
print("4: Perform citation analysis on a reference")
print("5: Extract text from PDF")

o1 = int(input('Choose an option:'))

if o1 == 2:
    in1 = '[' + str(input('Which reference to count:')) + ']'
    text = convert_pdf_to_txt('CCRO Citation’s Context & Reasons Ontology (1).pdf')
    print(text.count(in1))

if o1 == 5:
    print(convert_pdf_to_txt('CCRO Citation’s Context & Reasons Ontology (1).pdf'))

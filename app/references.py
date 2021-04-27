from refextract import extract_references_from_file
import pdfminer


def getReferences(path, title):
    references = extract_references_from_file(path)
    for reference in references:
        ref = 0
        if title in str(reference):
            for key,value in reference.items():
                if key == 'linemarker':
                    ref = int(''.join(filter(str.isdigit, str(value))))
            break
    return ref

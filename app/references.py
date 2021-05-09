from refextract import extract_references_from_file
import pdfminer


def getReferences(path, title):
    references = extract_references_from_file(path)
    ref = 0
    for reference in references:

        lowerRef = str(reference).lower()
        if title.lower() in lowerRef:
            for key,value in reference.items():
                if key == 'linemarker':
                    ref = int(''.join(filter(str.isdigit, str(value))))
            break
    return ref

import re
import spacy
from spacy.matcher import PhraseMatcher
from tokenizer import tokenize
from initModel import runAnalysis

nlp = spacy.load("en_core_web_sm")
#Using spacy to find and extract the sentences of a provided reference number for a file
def initialiseCitation(path,ref):


    f = open(path, "r")
    text = f.read()
    phrase_matcher = PhraseMatcher(nlp.vocab)
    #Phrases contains the list of instances to search for - [ref], [1,ref,2], [ref,1,2], [1,2,ref]
    phrases = ['['+ref+']',', ' + ref + ',', '[' + ref + ',', ',' + ref + ']']
    patterns = [nlp(text) for text in phrases]
    phrase_matcher.add('Cite', None, *patterns)
    return nlp(text), phrase_matcher
    f.close()

def searchCitation(path,ref, model):

    doc, phrase_matcher = initialiseCitation(path,ref)

    nCount = 0
    pCount = 0

    #The actual search code for the document
    for sent in doc.sents:
        for match_id, start, end in phrase_matcher(nlp(sent.text)):
            if nlp.vocab.strings[match_id] in ['Cite']:
                result = runAnalysis(sent.text, model)
                if result == 'Negative':
                    nCount = nCount + 1
                elif result == 'Positive':
                    pCount = pCount + 1
    return nCount,pCount


def countCitation(path,ref):
    doc, phrase_matcher = initialiseCitation(path,ref)

    countRef = 0

    for sent in doc.sents:
        for match_id, start, end in phrase_matcher(nlp(sent.text)):
            if nlp.vocab.strings[match_id] in ['Cite']:
                countRef = countRef + 1

    if countRef > 0:
        return countRef
    else:
        return 0

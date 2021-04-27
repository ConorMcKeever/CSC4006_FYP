import re
import spacy
from spacy.matcher import PhraseMatcher
from tokenizer import tokenize

def extractCitation(path,ref):
    nlp = spacy.load("en_core_web_sm")

    f = open(path, "r")
    text = f.read()

    phrase_matcher = PhraseMatcher(nlp.vocab)
    phrases = ['['+ref+']',', ' + ref + ',', '[' + ref + ',']
    patterns = [nlp(text) for text in phrases]
    phrase_matcher.add('Cite', None, *patterns)

    doc = nlp(text)
    finalText = ''

    for sent in doc.sents:
        for match_id, start, end in phrase_matcher(nlp(sent.text)):
            if nlp.vocab.strings[match_id] in ['Cite']:
                tokenize(sent.text)
    f.close()
    return finalText

def extractSentence(path,ref):
    f = open(path, "r")
    data = f.read()
    print([sentence + '.' for sentence in data.split('.') if '['+ref+']' in sentence])
    f.close()

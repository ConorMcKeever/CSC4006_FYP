import re
import spacy
from spacy.matcher import PhraseMatcher

def extractCitation(path,ref):
    nlp = spacy.load("en_core_web_sm")

    f = open(path, "r")
    text = f.read()

    phrase_matcher = PhraseMatcher(nlp.vocab)
    phrases = ['['+ref+']',', ' + ref + ',', '[' + ref + ',']
    patterns = [nlp(text) for text in phrases]
    phrase_matcher.add('Cite', None, *patterns)

    doc = nlp(text)

    for sent in doc.sents:
        num = 1
        for match_id, start, end in phrase_matcher(nlp(sent.text)):
            if nlp.vocab.strings[match_id] in ['Cite']:
                print(str(num) + '. ' + sent.text + '\n')
                num = num + 1

    f.close()

def extractSentence(path,ref):
    f = open(path, "r")
    data = f.read()
    print([sentence + '.' for sentence in data.split('.') if '['+ref+']' in sentence])
    f.close()

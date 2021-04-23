import spacy

def tokenize():
    nlp = spacy.load("en_core_web_sm")
    doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
    for token in doc:
        print(token.text)
import spacy

def tokenize(text):
    print("Tokenizing Text...")
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for token in doc:
        return token.text

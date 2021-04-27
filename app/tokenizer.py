import spacy

def tokenize(text):
    print("Tokenizing Text...")
    lemma_list = []
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for token in doc:
        lemma_list.append(token.lemma_)

    #Filter the stopword
    filtered_sentence =[]
    for word in lemma_list:
        lexeme = nlp.vocab[word]
        if lexeme.is_stop == False:
            filtered_sentence.append(word)

    #Remove punctuation
    punctuations="?:!.,;"
    for word in filtered_sentence:
        if word in punctuations:
            filtered_sentence.remove(word)
    print(filtered_sentence)

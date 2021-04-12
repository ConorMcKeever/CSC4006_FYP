import re

def extractSentence(path,ref):
    f = open('sample/' + path, "r")
    data = f.read()
    print([sentence + '.' for sentence in data.split('.') if ref in sentence])
    f.close()

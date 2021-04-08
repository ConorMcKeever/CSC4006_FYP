import re

def extractApple():
    txt="I like to eat apple. Me too. Let's go buy some apples."
    txt = "." + txt
    print(re.findall(r"([^.]*?apple[^.]*\.)",txt))

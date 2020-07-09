import re

def word_count(s):
    d = dict()
    s = s.lower().split()
    tokens = []
    for word in s:
        word = word.replace('"',"").replace(",", "").replace(".","")
        word = re.sub("[\W]+[\'\W]",'',word)
        if word:
            tokens.append(word)
    for token in tokens:
        if token not in d:
            d[token] = 1
        else: 
            d[token] += 1
    return d



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))

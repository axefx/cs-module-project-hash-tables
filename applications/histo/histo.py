import re
# `.items()` method on a dictionary might be useful.
# it's possible for `.sort()` to sort on multiple keys at once.
# negatives might help where `reverse` won't.
# you can print a variable field width in an f-string with
# nested braces, like so `{x:{y}}`
def clean_string(word_string):
    word_string = word_string.replace('"',"").replace(",", "").replace(".","")
    word_string = re.sub("[\W]+[\'\W]",'',word_string)
    return word_string


def histo(filename):
    d = dict()
    
    with open(filename) as f:
        filestring = f.read()
    
    word_list = filestring.lower().split()
    tokens = [ clean_string(word) for word in word_list ] 

    for token in tokens:
        if token not in d:
            d[token] = 1
        else: 
            d[token] += 1
    for word, count in sorted(d.items(), key=lambda items: -items[1])[:16]:
        print(f"{word}\t\t\t{'#'*count}")

if __name__ == "__main__":
    histo("robin.txt")
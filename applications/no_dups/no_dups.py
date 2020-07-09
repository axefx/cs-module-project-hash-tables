def no_dups(s):
    words = set()
    s = s.split()
    string = []
    for word in s:
        if word not in words:
            words.add(word)
            string.append(word)
    string = ' '.join(string)
    return string



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
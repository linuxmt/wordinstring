# -*- coding: utf-8 -*-
#!/usr/bin/env python
def wordinstring(string):
    global word
    strlen = len(string)
    wordlist = [] 
    word = ""
    for wis in range(0, strlen+1, +1):
        if string[wis:wis+1] not in " ":
            word = word + str(string[wis:wis+1])
        elif  (strlen == wis) and (word != ""):
              wordlist.append(word)
        else:
            if (word != ""):
                wordlist.append(word)
                word = ""
    return wordlist
print wordinstring("test deneme python")

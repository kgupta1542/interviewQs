#Refer to Daily Coding Problem #11

def autoComplete(string,words):
    length = len(string)
    elem = ""
    beg = ""
    
    for i in range(len(words)):
        elem = str(words[i])
        beg = elem[0:length]
        
        if string == beg:
            print(elem)
        
string = "de"
words = ["dog","deer","deal"]

autoComplete(string,words)

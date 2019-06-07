#\n - next line
#\t - indentation

def indentCounter(string): 
    i = 0
    while i < len(string):
        if string[i] == "\":
            break
        print(string[i])
        i += 1
    
    return i
        
path = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
print(indentCounter(path))
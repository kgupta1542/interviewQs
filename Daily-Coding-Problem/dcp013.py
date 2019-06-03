def substrUniqueChars(k, s):#k - number of unique characters, s - input string
    index = 0 #Starting index of substring
    maxLength = 0 #Max length of substring
    final = "" #Final substring
    
    for i in range(len(s)): #Run while the starting index is in bounds
        index = i #Move up the starting index
        uniqueCharCount = 0 #Set the amount of unique characters to 0
        temp = "" #Set the temporary string to a blank string
    
        while uniqueCharCount <= k and index < len(s): #Run while the amount of unique characters is correct and the ending index is in bounds
            if s[index] not in temp: #Check to see if character is unique
                uniqueCharCount += 1
            
            temp += s[index] 
            index += 1
        
        if maxLength < len(temp): #See if specific substring is longer than previous substrings
            maxLength = len(temp) - (uniqueCharCount - k)
            final = temp[0:len(temp) - (uniqueCharCount - k)]
            
    return maxLength, final

print(substrUniqueChars(2,"abcba")) #Should return (3, "bcb")

def decodeNumWays(inputString):
    length = len(inputString)
    countArr = [0,0]#[Even,Odd]
    #Even - pair begins on an even index; Odd - pair begins on an odd index
    count = 1#Account for when none of the pairs are used
    i = 0
    
    while i + 2 <= length:
        if int(inputString[i:i+2]) <= 26:#Make sure that the pair of 2 is decodable
            countArr[i%2] += 1#Add 1 to the corresponding group
            
        i += 1
    
    temp = 0.5 * countArr[0] * (countArr[0] + 1)#Add all permutations of evens
    count += temp
    temp = 0.5 * countArr[1] * (countArr[1] + 1)#Add all permutations of odds
    count += temp
    
    print(int(count))
        
decodeNumWays("111")#Should print 3 (aaa, ak, ka)

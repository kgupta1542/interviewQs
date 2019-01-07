def findMissingInt(x):#find lower and upper, checks if in x, declares as missing, finds smallest missing
	missing = 0
	temp = -1
	
	for i in range(len(x)):
		if x[i] >= 1:
			lower = x[i] - 1
			upper = x[i] + 1
			
			if upper in x or lower in x:#Fulfills last three reqs
				temp = upper*(upper not in x) + lower*(lower not in x)
		
			else:
				temp = lower*(lower != 0) + upper*(lower == 0)
			
			if (temp < missing or missing == 0) and temp != 0:
				missing = temp
	
	if temp == -1:
	    missing = 1
			
	return missing
	
numList = [1,3,6,4,2]#Missing Integer should be 2
missingInt = findMissingInt(numList)
print(missingInt)

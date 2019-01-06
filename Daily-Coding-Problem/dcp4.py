#no upper,  no lower     -->   return lower
#no upper,  yes lower    -->   return upper
#yes upper, no lower     -->   return lower
#yes upper,  yes lower   -->   return None

def findMissingInt(x):#find lower and upper, checks if in x, declares as missing, finds smallest missing
	missing = 0
	temp = -1
	
	for i in range(len(x)):
		if x[i] >= 1:
			lower = x[i] - 1
			upper = x[i] + 1
			
			if upper in x or lower in x:#Fulfills last three reqs
				temp = upper*(upper not in x) + lower*(lower not in x)
				
				if temp == 0:
					temp = None
		
			else:
				temp = lower*(lower != 0) + upper*(lower == 0)
			
			if (temp < missing and temp != None) or (missing == 0 and temp != None):
				missing = temp
			
	return missing
	
numList = [4,3,1,2]
missingInt = findMissingInt(numList)
print(missingInt)

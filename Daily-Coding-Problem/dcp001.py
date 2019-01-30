#Refer to Daily Coding Problem #1

def findSumInList(x,k):
	compls = [0] * (len(x))#Creates empty list of zeroes
	isTrue = False#Sets default value of boolean
	
	for i in range(len(x)):
		compl = k - x[i]#Finds the 'complement' of each element
		
		if x[i] in compls:#Checks if the element is the 'complement' of another number
			isTrue = True
			break#Ends loop as objective is completed
		
		compls[i] = compl
		
	return isTrue
			
numList = [10,15,3,7]
add = 17

sumIsInList = findSumInList(numList,add)
print(sumIsInList)

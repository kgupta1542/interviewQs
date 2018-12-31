def findSumInList(x,k):
	compls = [0] * (len(x))
	isTrue = False
	
	for i in range(len(x)):
		compl = k - x[i]
		
		if x[i] in compls:
			isTrue = True
			break
		
		compls[i] = compl
		
	return isTrue
			
numList = [10,15,3,7]
add = 17

sumIsInList = findSumInList(numList,add)
print(sumIsInList)

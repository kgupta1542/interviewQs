def multiplyNumsInList(x):
	product = 1
	outputList = [1] * len(x)
	output = []
	
	for i in range(len(x)):
		product *= x[i]
		outputList[i] = 1.0/x[i]
		
	output = [int(i * product) for i in outputList]
	return output

numList = [1,2,3,4,5]

output = multiplyNumsInList(numList)
print(output)

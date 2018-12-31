#Refer to Daily COding Problem #2

def multiplyNumsInList(x):
	product = 1#Setup with default values
	outputList = [1] * len(x)
	output = []
	
	for i in range(len(x)):
		product *= x[i]#Multiplies each element in list
		outputList[i] = 1.0/x[i]#Inserts reciprocal of element with corresponding index
		
	output = [int(i * product) for i in outputList]#Multiplies through reciprocal list with product as constant
	return output

numList = [1,2,3,4,5]

output = multiplyNumsInList(numList)
print(output)

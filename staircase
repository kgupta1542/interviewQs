#Problem Description: You have a staircase made up of N steps and the amount of steps that you can climb per step are in an array, X.
#Find and return the amount of possible ways that you can climb the staircase with the possible step sizes.

def numWays(n,x):#O(N) algorithm which optimizes storage space
	x.sort()#Sort step size array
	length = x[len(x)-1] - x[0] + 1#Find minimum storage for array
	nums = [0] * length
	nums[length-1] = 1#Set right-most unit of nums[] to most recent (position 0)

	for i in range(n):#Run for each value of n 
		sum = 0
		for j in x:#Run for each value in the step size array
			index = length - j#Find corresponding index in array
			sum += nums[index]#Add existing value from array (recursive math function)
		nums.pop(0)#Shifts array to 'current' position
		nums.append(sum)
		print(nums)
	return nums[length-1]#Returns the most recent unit (the nth position)

stepSize = [1,2]
steps = 14

possibleWays = numWays(steps,stepSize)

print(possibleWays)

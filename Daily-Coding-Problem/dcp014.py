import random

def pointInCircle(x, y, r): #Returns whether a point is inside or outside a circle
    inCircle = False
    
    sum = x*x + y*y
    if sum <= r*r:
        inCircle = True
        
    return inCircle

def monteCarloPi(): #Estimates the value of pi through a repetitive process
    inCircleCounter = 0
    totalCounter = 0
    R = 0.1
    
    for i in range(100000): #Generates 100,000 points
        pX = random.uniform(-0.1, 0.1)
        pY = random.uniform(-0.1, 0.1)
        
        if(pointInCircle(pX, pY, R) == True): #If in circle, increase inCircleCounter
            inCircleCounter += 1
        
        totalCounter += 1
        
    piApprox = 4*inCircleCounter/totalCounter
    return piApprox

print(monteCarloPi())
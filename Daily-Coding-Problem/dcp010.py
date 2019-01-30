#Refer to Daily Coding Problem #10

from threading import Timer

def jobScheduler(function, time):
    t = Timer(time/1000, function)
    t.start()
    
def write():
    print("Hello")

x = 1
print(x)
jobScheduler(write,5000)

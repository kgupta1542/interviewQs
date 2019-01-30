from threading import Timer

def jobScheduler(function, time):
    t = Timer(time/1000, function)
    t.start()
    
def write():
    print("Hello")

x = 1
print(x)
jobScheduler(write,5000)

On Wed, Dec 5, 2018 at 9:20 AM Daily Coding Problem <founders@dailycodingproblem.com> wrote:
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

Upgrade to premium and get in-depth solutions to every problem.

If you liked this problem, feel free to forward it along so they can subscribe here! As always, shoot us an email if there's anything we can help with!

No more? Unsubscribe.


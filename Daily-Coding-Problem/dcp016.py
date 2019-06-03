log = ["a1","b2,","c3"] #Sample log

def record(order_id): #Appends order_id to log[]
    log.append(order_id)
    
def get_last(i): #Returns the ith last term of log[]
    return log[len(log) - i]

record("d4")
print(log)

print(get_last(2))
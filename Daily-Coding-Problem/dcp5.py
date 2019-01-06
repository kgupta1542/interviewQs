def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(f):
	def first(a,b):
		return a
	return f(first)

def cdr(f):
	def second(a,b):
		return b
	return f(second)

print(car(cons(3,4)))
print(cdr(cons(3,4)))

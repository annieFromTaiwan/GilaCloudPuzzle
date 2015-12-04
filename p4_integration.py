
def test(x):
	return x

def anonymous(x):
	return x**2 + 1

def my_integrate(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	step_cnt = int( (end - start) / step )
	for _ in range(step_cnt):
		area += fun(intercept) * step
		intercept += step
	return area

def integrate(fun, start, end):
	step = 0.1
	intercept = start
	area = 0
	while intercept < end:
		intercept += step
		area += fun(intercept) * step
	return area

if __name__ == "__main__":
	#print (my_integrate(test, 0, 1))
	#print (integrate(test, 0, 1))

	#print (my_integrate(anonymous, 0, 10))
	print (integrate(anonymous, 0, 10))


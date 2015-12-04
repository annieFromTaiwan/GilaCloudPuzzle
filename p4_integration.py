
def test(x):
	return x

def anonymous(x):
	return x**2 + 1

# This version is more accurate than the orginial version and fits
# more to the 3rd wiki picture.
# Can't achieve this effect by only adding 1-3 lines to the original
# funciton without modifying other lines. That's why I made this new
# function
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


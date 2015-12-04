
cache = {}
def combination(n, r):
	if r==1:
		return n
	if n==r:
		return 1

	if (n, r) not in cache.keys():
		cache[(n, r)] = combination(n-1, r) + combination(n-1, r-1)
	return cache[(n, r)]


if __name__ == "__main__":
	print combination(40, 10)
	print combination(990, 33)

import math


test = []

def find_max_prime(N):
	composite_nums = set([])
	primes_of_N = set([])

	sqrt_N = int(math.sqrt(N))
	num = 3
	while True:
		num += 2
		if num > N:
			break

		if num in composite_nums:
			continue

		# num is a prime
		if N % num == 0:
			primes_of_N.add(num)
		while N % num == 0:
			N /= num
		composite_nums |= set( xrange(num, sqrt_N, num) )

	#print sorted(list(primes_of_N))
	return max(primes_of_N)


if __name__ == "__main__":
	#print find_max_prime(77)
	#print find_max_prime(13195)
	print find_max_prime(600851475143)

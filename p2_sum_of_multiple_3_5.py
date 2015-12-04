
def get_sum_of_multiple_3_5_below(n):
	n = n - 1
	cnt_3s = n/3
	sum_3s = (3 + cnt_3s*3) * cnt_3s / 2
	cnt_5s = n/5
	sum_5s = (5 + cnt_5s*5) * cnt_5s / 2
	cnt_15s = n/15
	sum_15s = (15 + cnt_15s*15) * cnt_15s / 2
	return sum_3s + sum_5s - sum_15s

def self_test():
	test_cases = {1:0, 2:0, 3:0, 4:3, 5:3, 6:8, 7:14, 8:14, 
			9:14, 10:23, 11:33, 12:33, 13:45}
	for q in test_cases:
		a = test_cases[q]
		print "Q: %d, A: %d, ans: %d" % (q, a, get_sum_of_multiple_3_5_below(q) )

if __name__ == "__main__":
	#self_test()
	print get_sum_of_multiple_3_5_below(1000)

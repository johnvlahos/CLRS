import time
import random

def rod_cutting_tester(rod_length):
	#px_list = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	px_list = [random.randint(0, 20) for i in range(rod_length)]
	print(px_list)


	def rod_cutting_recurse(rod_length, px_list):
		""" Given a rod with integral length and a list of prices for 
		lengths <= rod_length, determine the set of cuts that should be made
		to maximise the total price of all the pieces.

		Args:
			rod_length (int): n >= 0
			px (list): for  0 <= i <= rod_length, px[i] is the price for a rod of 
					   length i
		"""

		if rod_length == 0:
			return 0
		else:
			q = float("-inf")
			for interval in range(0, rod_length): 
				q = max(q, px_list[interval] + 
						   rod_cutting_recurse(rod_length - (interval + 1), px_list))
		return q


	
	def rod_cutting_memoized(rod_length, px_list, cache=None):
		""" A similar implementation to rod_cutting_recurse, but with caching
		to prevent identical decents into the recursion tree.
		"""

		if cache is None:
			cache = {}
		if rod_length in cache:
			return cache[rod_length]
		if rod_length == 0:
			q = 0
		else:
			q = float("-inf")
			for interval in range(0, rod_length): 
				q = max(q, px_list[interval] + 
						   rod_cutting_memoized(rod_length - (interval + 1), px_list, cache))
			cache[rod_length] = q
		return q

	# [0, 1, 5, 8, 10, 13]
	def rod_cutting_dp(rod_length, px_list):
		results = [0] * (rod_length + 1)
		for j in range(1, rod_length+1):
			q = float("-inf")
			for i in range(1, j+1):
				q = max(q, px_list[i-1] + results[j-i])
			results[j] = q
		return results[rod_length]

	for f in [rod_cutting_recurse, rod_cutting_memoized, rod_cutting_dp]:
		start = time.time()
		print("max sum of prices for length == {} using {}: {} ({})".format(rod_length, f, f(rod_length, px_list), time.time() - start))
		
	print("\n")


for i in range(10, 20):
	rod_cutting_tester(i)

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

def rod_cutting(rod_length):
	px_list = [1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
	return rod_cutting_recurse(rod_length, px_list)


for i in range(11):
	print("Max sum of prices for length == {}: {}".format(i, rod_cutting(i)))

def is_curzon(num):
	eqn01 = pow(2, num) + 1
	eqn02 = 2*num + 1 

	return eqn01 % eqn02 == 0
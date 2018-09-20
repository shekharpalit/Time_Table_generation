memo = {}
def power(b ,e):
	if e in memo :
		return memo[e]
	else :
		p = b * power(b, e-1)
	memo[e] = p

	return p


power(2,3)
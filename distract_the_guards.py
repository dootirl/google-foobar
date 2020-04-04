def gcd(x, y):
	while (y):
		x, y = y, x % y
	return x

def wrestle(x, y):
	z = (x + y) // gcd(x, y)
	return bool(z & z - 1)

def solution(banana_list):
	

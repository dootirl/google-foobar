def soe():
	D = {}
	q = 2

	while True:
		if q not in D:
			yield q
			D[q * q] = [q]
		else:
			for p in D[q]:
				D.setdefault(p + q, []).append(p)
			del D[q]

		q += 1

def solution(n):
	primes = soe()
	tmp = ""

	for i in primes:
		tmp += str(i)
		if len(tmp) > n + 4:
			return tmp[n:n + 5]

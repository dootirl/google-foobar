def solution(M, F):
	gen = 0
	m, f = int(M), int(F)
	h, l = max(m, f), min(m, f)
	
	while h != 1:
		if h % l == 0:
			return "impossible"
		gen += h // l
		m, f = h % l, l
		h, l = max(m, f), min(m, f)
	return gen - 1

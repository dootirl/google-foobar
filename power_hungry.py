def solution(xs):
    maxp = 1
    negs = []

    for i in xs:
        if i < 0:
            negs.append(i)
        elif i > 1:
            maxp *= i
    if len(negs) < 2 and max(xs) < 2:
        return str(max(xs))
    negs.sort()
    while len(negs) > 1:
        maxp *= negs.pop(0) * negs.pop(0)
    return str(maxp)

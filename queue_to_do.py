def solution(start, length):
    cutoff = length
    value = start
    checksum = 0

    while cutoff > 0:
        checksum ^= series_xor(value) ^ series_xor(value + cutoff)
        value += length
        cutoff -= 1

    return checksum

def series_xor(n) : 
    if n == 0:
        return 0

    n -= 1

    if n % 4 == 0: 
        return n 
    if n % 4 == 1: 
        return 1
    if n % 4 == 2: 
        return n + 1
    return 0

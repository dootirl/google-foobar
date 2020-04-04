def parent(height, node):
    size = 2 ** height - 1    
    
    if node == size:
        return -1

    before = 0

    while True:
        if size == 0:
            break
        
        size >>= 1
        left = before + size
        right = left + size
        me = right + 1
        
        if left == node or right == node:
            return me
        if node > left:
            before = left

def solution(h, q):
    return [parent(h, i) for i in q]

nolog = 0

def log(s):
    if nolog:
        return
    print(s)

def solution(l, t):
    l_size = len(l)
    for cursor_pos in range(0, l_size):
        cursor_sum = 0
        for cursor_size in range(0, l_size - cursor_pos):
            cursor_end = cursor_pos + cursor_size
            cursor_sum += l[cursor_end]
            if cursor_sum == t:
                return [cursor_pos, cursor_end]
            elif cursor_sum > t:
                break
    return [-1, -1]

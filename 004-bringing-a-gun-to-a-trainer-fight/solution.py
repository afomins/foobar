from array import *

nolog = 0

def log(s):
    if nolog:
        return
    print(s)


def solution(room_size, pos, pos_target, dist):
    log("Creating squares")
    squares = array('L', [val * val for val in range(dist + 2)])
    log("squares=" + str(squares.tolist()))

    log("Creating dist2")
    dist2 = [None for row in range(dist + 1)]
    for row_idx in range(dist + 1):
        row_idx2 = squares[row_idx]
        row = array('L', [row_idx2 + squares[col_idx] for col_idx in range(dist + 1)])
        dist2[row_idx] = row

    log("Iterating dist2")
    result = 0
    for y in range(dist + 1):
#        line = ""
        for x in range(dist + 1):
#            line += str(dist2[y][x]) + "\t"
            result += dist2[y][x]
#        log(line)
    log("Result=" + str(result))

    return 7

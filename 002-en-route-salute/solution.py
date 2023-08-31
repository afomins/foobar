nolog = 0

def log(s):
    if nolog:
        return
    print(s)

def walk_hallway(hallway, begin, dir):
    salutes = 0
    for pos in range(begin, -1 if dir < 0 else len(hallway), dir):
        unit = hallway[pos]
        if dir < 0 and unit == '>': # go left
            salutes += 1
        elif dir > 0 and unit == '<': # go right
            salutes += 1

    log("  begin=" + str(begin) + " dir=" + str(dir) + " salutes=" + str(salutes))
    return salutes

def solution(hallway):
    salutes = 0
    for pos in range(0, len(hallway)):
        unit = hallway[pos]
        if unit not in ('>', '<'):
            continue
        salutes += walk_hallway(hallway, pos, +1 if unit == '>' else -1)
    return salutes

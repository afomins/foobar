nolog = 0

def log(s):
    if nolog:
        return
    print(s)

def prev_gen(m, f):
    gen_num = 0
    if m <= 0 or f <= 0:
        pass # errro
    elif m == f:
        pass # error
    elif m > f:
        diff = m - f
        gen_num = 1 if diff <= f else diff / f
#        gen_num = 1
        m -= f * gen_num
    elif f > m:
        diff = f - m
        gen_num = 1 if diff <= m else diff / m
#        gen_num = 1
        f -= m * gen_num

    return gen_num, m, f

def solution(m, f):
    m = int(m)
    f = int(f)
    gen = 0
    while True:
        if m == f == 1:
            break # bingo

        gen_num, m, f = prev_gen(m, f)
        log("  gen=" + str(gen) + "+" + str(gen_num) + "=" + str(gen + gen_num) + " bombs=(" + str(m) + ", " + str(f) + ")")

        if gen_num == 0:
            gen = None # impossible
            break

        gen += gen_num
    return "impossible" if gen == None else str(gen)

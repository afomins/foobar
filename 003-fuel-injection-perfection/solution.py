nolog = 0

def log(s):
    if nolog:
        return
    print(s)

def is_even(val):
    return val & 1 == 0

def get_bit_len(val, mask):
    len = 0
    while val:
        if val & 1 == mask:
            len += 1
            val_prev = val
            val >>= 1
#            log("{0:b}".format(val_prev) + " -> " + "{0:b}".format(val))
        else:
            break
    return len

def solution(n_str):
#    n = 111
#    next = get_bit_len(111 + 1, 0)
#    prev = get_bit_len(n - 1, 0)
#    log("next = " + str(next))
#    log("prev= " + str(prev))
#    return 1
    
    n = long(n_str)
    log("n = " + str(n) + "\t\t\t\t" + "{0:b}".format(n))

    op_num = 0
    while n != 1:
        op = "xxx"
        n_prev = n
        if n == 0:
            n = 1
            op = " bingo0 "

        elif n == 3:
            n = 2
            op = " bingo3 "

        elif is_even(n):
            n >>= 1
            op = " / 2"
        else:
            next = get_bit_len(n + 1, 0)
            prev = get_bit_len(n - 1, 0)

            if next > prev:
                n += 1
                op = " + 1"
            else:
                n -= 1
                op = " - 1"

        log(str(n_prev) + op + " = " + str(n) + "\t\t\t" + "{0:b}".format(n))
        op_num += 1

    return op_num

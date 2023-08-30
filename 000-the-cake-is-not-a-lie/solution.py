nolog = 0

def log(s):
	if nolog:
		return
	print(s)

def get_divisors(value):
	log(">>> get_divisors(" + str(value) + ")")
	divisors = []
	for i in range(1, value):
		if value % i == 0:
			divisors.append(i)
			log(" d=" + str(i))
	return divisors

def get_max_equal_parts(divisors, input):
    log(">>> get_max_equal_parts(" + input + ")")

    for cursor_size in divisors:
        cursor = input[0:cursor_size]
        cursor_pos = 0
        step_num = len(input) / cursor_size
        bingo = True
        for xxx in range(0, step_num):
            candidate = input[cursor_pos:cursor_pos+cursor_size]
            if cursor != candidate:
        	    bingo = False
        	    break
            cursor_pos += cursor_size

        log(" cursor=" + cursor +" bingo=" + str(bingo))
        if bingo:
        	return step_num

    return 1


def solution(s):
    if not isinstance(s, str):
        return 0

    divisors = get_divisors(len(s))
    part_num = get_max_equal_parts(divisors, s)

    log(" part_num=" + str(part_num))
    return part_num

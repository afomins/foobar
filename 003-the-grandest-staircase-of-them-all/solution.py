nolog = 0

def log(s):
    if nolog:
        return
    print(s)

dic = {}
def p(n, k):
    """Gives the number of ways of writing n as a sum of exactly k terms or, equivalently, 
    the number of partitions into parts of which the largest is exactly k.  
    """
    if n < k:
        return 0
    if n == k:
        return 1
    if k == 0:
        return 0
    
    key = str(n) + ',' + str(k)
    try:
        temp = dic[key]
    except:
        temp = p(n-1, k-1) + p(n-k, k)
        dic[key] = temp
    finally:
        return temp

def partitions_count(n, base):
    """Gives the number of ways of writing the integer n as a sum of positive integers,
    where the order of addends is not considered significant.
    """
    partitions_count = 0
    for k in range(base + 1):
        ppp = p(n, k)
        log(  "n=" + str(n) + " k=" + str(k) + " -> " + str(ppp))
        partitions_count += ppp
    return partitions_count


def solution(block_max_num):
#    return partitions_count(block_max_num)

    staircase_num = 0
    block_num = 3
    base = 2
    while True:
        block_extra = block_max_num - block_num
        if block_extra == 0:
            partition_num = 1
#        elif block_extra <= base:
#            partition_num = block_extra
        else:
            partition_num = partitions_count(block_extra, base)
        staircase_num += partition_num

        log("base=" + str(base) + " block_num=" + str(block_num) + " block_extra=" + str(block_extra) + " partition_num=" + str(partition_num) + " staircase_num=" + str(staircase_num))

        base += 1
        block_num += base

        if block_num > block_max_num:
            break

    return staircase_num

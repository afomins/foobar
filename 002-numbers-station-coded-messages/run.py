from solution import *

args = ( 
    ([1, 2, 3, 4], 15),
    ([4, 3, 10, 2, 8], 12)
)

for a in args:
    log("---------")
    l = a[0]
    s = a[1]
    log(" >>> solution(" + str(l) + ", " + str(s) + ")")
    ret = solution(l, s)
    log("  return=" + str(ret))

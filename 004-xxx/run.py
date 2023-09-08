from solution import *

args = ( 
    1,
    2,
)

for a in args:
    log("---------")
    log(" >>> solution(" + str(a) + ")")
    ret = solution(a)
    log("  return=" + str(ret))

from solution import *

args = (
    3,
    4,
    5,
    6, 
    7, 
    8,
    9,
    10,
#    200,
)

for a in args:
    log("---------")
    log(" >>> solution(" + str(a) + ")")
    ret = solution(a)
    log("  return=" + str(ret))

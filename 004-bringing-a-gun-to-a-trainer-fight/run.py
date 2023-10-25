from solution import *

args = (
    ([3, 2], [1, 1], [2, 1], 4),
#    ([300,275], [150,150], [185,100], 500),
)

for a in args:
    log("---------")
    log(" >>> solution(" + str(a) + ")")
    ret = solution(*a)
    log("  return=" + str(ret))

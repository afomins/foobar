from solution import *

args = (
    ([3, 2], [1, 1], [2, 1], 4),
#    ([5, 4], [2, 2], [2, 3], 100),
#    ([5, 4], [2, 2], [2, 3], 10000),
#    ([300,275], [150,150], [185,100], 500),
#    ([1250,1250], [150,155], [185,1003], 10),

#    ([5, 5], [2, 1], [2, 3], 5),    # up
#    ([5, 5], [2, 3], [2, 1], 6),    # down
#    ([5, 5], [1, 2], [4, 2], 2),    # right
#    ([5, 5], [4, 2], [1, 2], 5),    # left
)

for a in args:
    log("---------")
    log(" >>> solution(" + str(a) + ")")
    ret = solution(*a)
    log("  return=" + str(ret))

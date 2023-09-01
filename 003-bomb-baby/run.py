from solution import *

args = ( 
    ('2', '1'), # 1
    ('2', '4'), # impossible
    ('4', '7'), # 4
    ('2', '1'), # 1
    ('10', '3'), # 1
    ('3', '1'), # 1
)

for a in args:
    log("---------")
    m = a[0]
    f = a[1]
    log(" >>> solution(" + m + ", " + f + ")")
    ret = solution(m, f)
    log("  return=" + ret)

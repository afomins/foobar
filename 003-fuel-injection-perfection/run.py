from solution import *

args = ( 
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "10",
    "11",
    "12",
    "13",
    "14",
    "15",
    "16",
    "17",

    "93", #str(int("1011011", 2)),
#    str(int("10011001", 2)),
#    "10597634857634786534786348765348765348763487653487" "20597634857634786534786348765348765348763487653487"
#    "30597634857634786534786348765348765348763487653487" "40597634857634786534786348765348765348763487653487"
#    "50597634857634786534786348765348765348763487653487" "60597634857634786534786348765348765348763487653487"
#    "123456789"
)

for m in args:
    log("---------")
    log(" >>> solution(" + str(m) + ")")
    ret = solution(m)
    log("  return=" + str(ret))
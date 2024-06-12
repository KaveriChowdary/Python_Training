import math

def ispsq(n):
    s = int(n**0.5)
    return s*s == n

n = int(input("n: "))
flag = True

for i in range(2, int(math.sqrt(n)) + 1):
    if n % i == 0:
        if ispsq(i) or ispsq(n // i):
            print("not square free")
            flag = False
            break

if flag:
    print("square free")
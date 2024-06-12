n=int(input())
def printNumber(n):
    if n <=0:
        return
    printNumber(n-1)
    print(n, end = ' ')
printNumber(n)
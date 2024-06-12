'''def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n < 0 :
        print("incorrect input")
    elif n == 1 or n==2:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)'''
#n=int(input())
#print(fibonacci_recursive(n))


#2 dynamic programming
fibval=[0,1]
def fib(n):
    if n <0:
        print("incorrect value")
    elif n <len(fibval):
        return fibval[n]
    fibval.append(fib(n-1)+fib(n-2))
    return fibval[n]
print(fib(int(input())))

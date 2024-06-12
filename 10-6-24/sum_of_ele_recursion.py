#sum of all elements in array using recursion
def sum_recursion(a):
    if not a:
        return 0
    else:
        return a[0]+sum_recursion(a[1:])
a=list(map(int,input().split()))
print(sum_recursion(a))
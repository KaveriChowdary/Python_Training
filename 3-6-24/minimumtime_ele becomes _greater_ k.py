'''Micro purchased an array A having N integer values. After playing it for a while, he got bored of it and
decided to update value of its element. In one second he can increase value of each array element by 1. He wants
each array element's value to become greater than or equal to K. Please help Micro to find out the minimum amount of time
it will take, for him to do so.

Input:
First line consists of a single integer, T, denoting the number of test cases.
First line of each test case consists of two space separated integers denoting N and K.
Second line of each test case consists of N space separated integers denoting the array A.

Output:
For each test case, print the minimum time in which all array elements will become greater than or equal to K.
Print a new line after each test case.
'''
def add(a, n, k):
    count = 0
    for i in range(n):
        a[i] = a[i] + 1
        count += 1
    p = min(a)
    if p >= k:
        return count
    else:
        return add(a, n, k)

def min(a):
    m = float('inf')
    for num in a:
        if num < m:
            m = num
    return m

t = int(input())
while t > 0:
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    ans = add(a, n, k)
    print(ans)
    t -= 1

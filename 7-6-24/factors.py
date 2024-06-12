'''kth Largest factor of N

Problem Description
Question -: A positive integer d is said to be a factor of another posi N is divided by d, the remainder obtained is zero.
For example, for n factors 1, 2, 3, 4, 6, 12. Every positive integer k has at least two facto k itself. Given two positive
integers N and k, write a program to print factor of N.
input : 12 3
output : 4
'''
n,k=map(int,input().split())
for deno in range(n,0,-1):
    if n %deno ==0:
        k-=1
    if k==0:
        print(deno)
        break
if k!=0:
    print('1')
    
 
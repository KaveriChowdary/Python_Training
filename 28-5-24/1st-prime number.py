#prime num or not
n=int(input())

#1 o(n)
c=0
for i in range(1,n+1):
    if n % i == 0:
        c+=1
if c==2:
    print("prime")
else:
    print("not a prime")
    
#2 o(1)-best , o(n)-worst case
for i in range(2,n):
    if n % i ==0:
        print("not a prime")
        break
else:
    print("prime")

#3
for i in range(2,(n//2)+1):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")

#4 o(sqrt(n))
for i in range(2,int(n**0.5)+1):
    if n % i ==0:
        print("not prime")
        break
else:
    print("prime")
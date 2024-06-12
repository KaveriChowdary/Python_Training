a=list(map(int,input().split()))
b=list(map(int,input().split()))
a.sort()
b=sorted(b)[::-1]#sorted(b).reverse()
res=0
for i in range(len(a)):
    res+=a[i]*b[i]
print(res)
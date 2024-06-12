#program to sort frist half in ascending order and second half in descending order in an array
l=list(map(int,input().split()))
n=len(l)
res=sorted(l)[:n//2]
res+=sorted(l,reverse =True)[:n//2]
print(res)
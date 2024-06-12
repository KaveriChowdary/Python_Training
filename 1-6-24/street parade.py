n=int(input())
t = list(map(int,input().split()))
s=[]
r=[]
for i in range(0,len(t)-1):
    if t[i] > t[i+1]:
        s.append(t[i])
    else:
        r.insert(0,t[i])
r.insert(0,t[-1])
r=s+r
if sorted(t,reverse=True) == r:
    print("yes")
else:
    print("no")
    
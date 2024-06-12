n,t=map(int,input().split())
s=input()
q=list(s)
for g in range(t):
    i=0
    while i<n-1:
        if q[i] == 'B' and q[i+1] =='G':
            q[i],q[i+1] = q[i+1],q[i]
            i+=1
        i+=1
print(''.join(q))
        
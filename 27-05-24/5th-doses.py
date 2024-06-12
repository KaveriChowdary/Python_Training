#doses
#n=list(map(int,input().split()))
#k=int(input())
#r=max(n)-k
#print(r)

#number of consecutive 1s in list
nums=[1,1,0,1,1,1]
c,maxval=0,0
for i in nums:
    if i==1:
        c+=1
        if c > maxval:
            maxval=c
    else:
        c=0
print(maxval)
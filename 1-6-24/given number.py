t=int(input())
for i in range(t):
    n=int(input())
    numList=list(map(int,input().split()))
    index=n-1
    for i in range(n-1,-1,-1):
        if numList[i]>numList[i-1]:
            numList[i],numList[i-1]=numList[i-1],numList[i]
            index=i
            break
    res=[str(ele) for ele in (numList[:index]+(numList[index:])[::-1])]
    print(''.join(res))
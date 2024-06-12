num=int(input())
events=list(map(int,input().split()))
avaPolice=0
unEvents=0
for event in events:
    if event>0:
        avaPolice+=event
    elif event ==-1:
        if avaPolice <= abs(event):
            unEvents=abs(event)-avaPolice
            avaPolice=0
        else:
            avaPolice-= abs(event)
print(unEvents)
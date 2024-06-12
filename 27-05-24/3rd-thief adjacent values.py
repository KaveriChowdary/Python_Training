'''ps :there are n houses build in a line ech of which contais some value in it . a thief is going to steal the maximal
values of hpouses , but he cant steal in adjacent houses beause the owner of stolen house will tell his two neig
 left and right side
 in={6,7,1,3,8,2,5}
 ou=20 i.e 7+8+5=20'''

house=list(map(int,input().split()))
emax=sum(house[0::2])
omax=sum(house[1::2])
tmax=0
while(max(house)!=0):
    tmax+=max(house)
    i=house.index(max(house))
    if i == 0:
        house[0],house[1]=0,0
    elif i ==  len(house)-1:
        house[-2],house[-1] = 0 , 0
    else:
        house[i],house[i+1],house[i-1] =0,0,0
print(max([omax,emax,tmax]))
'''ps : take input of list contains list and print the index of list which have highest sum value'''
n=int(input())
l=[]
nestlist = [list(map(int,input().split())) for i in range(n)]
print(nestlist)
maxin , tsum = 0 , 0
for index,data in enumerate(nestlist):
    if tsum <sum(data):
        tsum =sum(data)
        maxin = index
print(maxin)
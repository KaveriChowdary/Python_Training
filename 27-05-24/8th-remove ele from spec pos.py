'''ps: take input of a tuple and the position of ele to be removed and output should the list after deleting the ele'''
mydata=tuple(input().split())
i = int(input())
#1
inlist = list(mydata)
inlist.pop(i)
print(tuple(inlist))
#2
print(mydata[:i]+mydata[i+1:])
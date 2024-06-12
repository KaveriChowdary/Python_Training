#take a number as input and print the output accord to lexicographical order
n=int(input())
m=[]
l=[]
for i in range(1,n+1):
    l.append(str(i))
l.sort()
print(list(map(int,l)))
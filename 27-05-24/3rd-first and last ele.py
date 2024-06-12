#take a list and swap the first and last element
l=list(input().split())
f=l[0]
l[0]=l[-1]
l[-1]=f
#l[0],l[-1] = l[-1] , l[0]
print(l)
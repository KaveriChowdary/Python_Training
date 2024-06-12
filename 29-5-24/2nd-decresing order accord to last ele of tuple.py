#python program to get a list ,sorted in decreasing order by the last element in each tuple from a given list
#non -empty tuples
#input: [(2,5),(1,2),(4,4),(2,3),(2,1)]
#out:[(2,1),(1,2),(2,3),(4,4),(2,5)]

def end(l):
    return l[-1]
n=int(input())
l=[tuple(map(int,input().split())) for i in range(n)]
print(l)
res= sorted(l,key=end)
print(res)
#python program to remove all consecutives duplicates from a string
s = "aabbsca"
res=s[0]
t=s[0]
for i in s[1:]:
    if i!=t:
        res+=i
        t=i
print(res)
        
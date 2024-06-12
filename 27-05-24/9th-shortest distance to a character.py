#shortest distance to a character qn0-821 (leetcode)
#1
def shortestToChar(s, c):
        appear = [i for i in range(len(s)) if s[i]==c]
        return [abs(min(appear,key=lambda x: abs(x-i))-i) for i in range(len(s))]
s="aaab"
c="b"
print(shortestToChar(s,c))

#2
clist=[]
rlist=[]
for i in range(len(s)):
    if s[i]==c:
        clist.append(i)
for i in range(len(s)):
    rlist.append(min([abs(x-i) for x in clist]))
return rlist
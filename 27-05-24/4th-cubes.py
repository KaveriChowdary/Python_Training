l=[]
for i in range(1,6):
    k=i*i*i
    l.append(k)
print(l)
cubelist=[i*i*i for i in range(1,6) if i %2==0]
print(cubelist)

data="hello everyone"
s=[]
for i in range(len(data)):
    if i%2!=0:
        s.append(data[i])
print(s)
d=[]
for ch in data[1::2]:
    d.append(ch)
print(d)
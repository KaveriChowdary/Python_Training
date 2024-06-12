import string
s="123av5b4"
c=0
n=""
for i in s:
    if i in string.digits:
        n+=i
if n=="":
    print(0)
else:
    print(int(n))
        
        
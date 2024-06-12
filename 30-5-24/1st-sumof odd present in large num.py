#print sum of odd numbers present in a large number
#inp:3446877846445566
#out:27
#1
n=input()
s=0
for i in n:
    if int(i) % 2 !=0:
        s=s+int(i)
print(s)

#2
num=int(input())
s2=0
while num !=0:
    r=num%10
    if r %2!=0:
        s2+=r
    num//=10
print(s2)

#3
num3=input()
oddlist =['1','3','5','7','9']
tos=0
for i in num3:
    if i in oddlist:
        tos+=int(i)
print(tos)
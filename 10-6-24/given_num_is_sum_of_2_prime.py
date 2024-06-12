#check whether a given num can be represented as sum of 2 prime numbers
num=int(input())
def isPrime(deno=2):
    if num <2 :
        return False
    if deno == int(num **0.5) +1:
        return True
    if num % deno == 0:
        return False
    return isPrime(deno+1)
plist=[i for i in range(2,num+1) if isPrime(i)]
flag=False
for i in range(len(plist)):
    for ele in plist[i::-1]:
        if sum([plist[i],ele])==num:
            flag=True
            break
if flag:
    print('yes')
else:
    print('no')
    
            
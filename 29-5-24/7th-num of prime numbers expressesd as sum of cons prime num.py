'''some prime numbers can be expressed as sum of other consecutive prime numbers
eg 5=2+3
17=2+3+5+7
your task is to find how many prime numbers which satisfy the property are present in range oof 3 to N
subject to a consstraint that summationshould always start with number 2
write a code to find out the number of prime numbers that satisfy the above mentioned property in given range
'''
def isPrime(num):
    if num==0 or num==1:
        return False
    for deno in range(2,int(num**0.5)+1):
        if num%deno ==0:
            return False
    return True
num=int(input())
primelist=[i for i in range(2,num+1) if isPrime(i)]
count , psum = 0, primelist[0]
for p in primelist[1:]:
    psum+=p
    if psum > num :
        break
    if isPrime(psum):
        count+=1
print(count)  
    
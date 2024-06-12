num=int(input())
def isPrime(deno=2):
    if num <2 :
        return False
    if num % deno == 0:
        return False
    if deno == int(num **0.5) +1:
        return True
    return isPrime(deno+1)
print(isPrime())
    
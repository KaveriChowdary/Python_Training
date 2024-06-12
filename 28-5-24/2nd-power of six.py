#given an integer n , return true if it power of 6 else return false
n=int(input())
while n!=1:
    if n % 6==0:
        n//=6
    else:
        print("false")
        break
else:
    print("true")
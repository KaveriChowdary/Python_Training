import string
print(string.ascii_letters)
print(string.hexdigits)
print(string.digits)
print(string.octdigits)

#check if data is number or not
s ="abh"
for i in s:
    if i in string.digits :
        print("yes")
        break
    else:
        print("no")
        break
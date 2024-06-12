#print true if the given string is palindrome els eno using stack
s=input()
stack=list(s)
print(stack)
for i in s:
    if stack.pop() !=i:
        print("not a palindrome")
        break
else:
    print("palindrome")
    
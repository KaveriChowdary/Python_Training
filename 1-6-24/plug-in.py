#81A -codeforces
dstr=input()
stack=[]
for i in dstr:
    if stack and stack[-1] == i:
        stack.pop()
    else:
        stack.append(i)
print(''.join(stack))

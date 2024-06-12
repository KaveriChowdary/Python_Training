s= "hey hi"
def reverses(s):
    if len(s)==0:
        return s
    return s[-1]+reverses(s[:-1])
print(reverses(s))
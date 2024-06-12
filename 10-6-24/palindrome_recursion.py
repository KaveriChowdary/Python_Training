#palindrome or not using recursion
def palindrome_rec(s):
    if len(s) <=1:
        return True
    if s[0]==s[-1]:
        return palindrome_rec(s[1:-1])
    else:
        return False
s=input()
print(palindrome_rec(s))

#display the largest palindrome from given number
#in: 120021 out : 120021
#in: 12210 out:1221
#in: 12345 out:1
#in: 12344 out: 44
#in: 12011221 out :1221
def largestPal():
    maxlen=0
    larpal=''
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            substr =s[i:j]
            if palindrome_rec(substr):
                if len(substr) > maxlen:
                    maxlen = len(substr)
                    larpal=substr
    return larpal
print(largestPal())
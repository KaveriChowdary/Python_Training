'''rotate a given string in spec direction by specified magnitude after each rotation make a note of the first character of
rotated string, after all rotation performed the accumulated string formed by first characters of the strings is
the FIRSTCHARSTRING will be produced and check if the string is anagram of any substring
of the given string if yes print yes else no
input:
carrace
3 -no of rotations
l 2 -left side 2 characters   "carrace"---> rraceca -2 chars rotated left
r 2                           "carrace"---> cecarra -rotated right
l 3                           "carrace" ---> racecar -rotated left
by taking the firts charcter from strings we get "rcr" as a string
out:no
explanation:
after applying all the rotations the string will be "rcr" which is not a anagram of any sub
string of origial string "carrace"'''

#1
s = input()
rot = int(input())
res=''
for i in range(rot):
    dr , mag = input().split()
    if dr.upper() == 'L':
        res+=(s[int(mag):]+s[:int(mag)])[0]
    elif dr.upper() =='R':
        res+= (s[:int(mag)]+s[int(mag):])[0]
sublist=[s[i:i+rot] for i in range(0,len(s)-rot+1)]
#anagram
for i in sublist:
    if sorted(i)==sorted(res):
        print("yes")
        break
else:
    print("no")

#2

from collections import deque
qstr=deque(input())
rot=int(input())
res=""
for i in range(rot):
    di,mag =input().split()
    if di== 'l' or di =='L':
        qstr.rotate(-int(mag))
        res+=qstr[0]
    elif di =='r' or di=='R':
        qstr.rotate(int(mag))
        res+=qstr[0]
sublist=[s[i:i+rot] for i in range(0,len(s)-rot+1)]
for i in sublist:
    if sorted(i) == sorted(res):
        print("yes")
        break
else:
    print("no")





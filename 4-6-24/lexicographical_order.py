'''Little Jill jumbled up the order of the letters in our dictionary. Now, Jack uses this list to find the smallest
lexicographical string that can be made out of this new order. Can you help him?
You are given a string P that denotes the new order of letters in the English dictionary.
You need to print the smallest lexicographic string made from the given string S.
Constraints: 1 <= T <= 1000
Length (P) = 261 <= length (S) <= 100
All characters in the string S, P are in lowercase
Input Format:
The first line contains number of test cases T
The second line has the string P
The third line has the string S
Output:
Print a single string in a new line for every test case giving the result'''

t=int(input())
test_cases = []
for _ in range(t):
    # Read the strings P and S for each test case
    P = input().strip()
    S = input().strip()
    test_cases.append((P, S))
str=""
for i, (P, S) in enumerate(test_cases):
    for i in P:
        if i in S:
            str=str+i
    print(str)
    str=""
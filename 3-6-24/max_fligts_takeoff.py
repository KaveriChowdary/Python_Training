'''Sandhir was into aviation industry and she was trying to check with some take off rules. There are three planes
A, B and C. Plane A will takeoff on every pth day i.e. p, 2p, 3p and so on. Plane B will takeoff on every qth day and plane C
will takeoff on every rth day. There is only one runway and the takeoff timing is same for each of the three planes on each day. Now her task is to find out the maximum number of flights that will successfully takeoff in the period of N days.
Note: If there is collision between the flights no flight will take off on that day.
input:
The first line of the input contains a single integer T, the number of test cases 4
Then T lines follow each containing four space-separated integers N , p ,q and
r as denoted in the statement.
Output Format:
For each test case print a single integer representing the max number 
of flights that will successfully takeoff in the period of n days
'''
tcase=int(input())
tsum=0
for i in range(tcase):
    days,p,q,r = list(map(int,input().split()))
    for i in range(1,days+1):
        a=i%p
        b=i%q
        c=i%r
        if a==0 or b==0 or c==0:
            if a==0 and b==0:
                continue
            elif a==0 and c==0:
                continue
            elif b==0 and c==0:
                continue
            tsum+=1
    print(tsum)
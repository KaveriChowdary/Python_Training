#remove the empty tuples
mydata = [(),(),('',),(1,2,3),(5,1)]
mydata = [i for i in mydata if i and all(i)]
print(mydata)
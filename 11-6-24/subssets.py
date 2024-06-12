nums = [1,3] # {[],[5],[6],[1],[1,5],[1,6],[5,6],[5,1,6]}
def allsub():
    res = [[]]
    for i in range(len(nums)):
        for j in range(i+1,len(nums)+1):
            res.append(nums[i:j])
    return res
print(allsub())
#2
from itertools import combinations
subsets=[]
for i in range(len(nums)+1):
   subsets.extend(combinations(nums, i))
print(subsets)
xor_results=[]
for subset in subsets:
    xor_result = 0
    for num in subset:
        xor_result ^= num
    xor_results.append(xor_result)
print(sum(xor_results))

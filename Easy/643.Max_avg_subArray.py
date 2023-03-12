nums = [1,12,-5,-6,50,3]
k = 4
# nums = [5]
# k = 1
#  [1,12,-5,-6,50,3]
nums = [4,2,1,3,3]
k=2

def findMaxAverage(nums, k):
    left =0
    sm = sum(nums[left:k])
    maxAvg = sm/k
    for i in range(k,len(nums)):
        sm = (sm -nums[left] + nums[i])
        newAvg = sm /k
        maxAvg = max(maxAvg,newAvg)
        left +=1
    return maxAvg

print(findMaxAverage(nums,k))

# Passed
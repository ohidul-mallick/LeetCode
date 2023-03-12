nums = [5,7,7,8,8,10]
target = 8
# nums = [5,7,7,8,8,10]
# target = 6
# nums = [1,4]
# target = 4
# nums = [3,3,3]
# target = 3

def searchRange(nums, target):
    if target not in nums:
        return [-1,-1]
    indL = nums.index(target)
    nums[indL] = -1
    indR=indL
    while(target in nums):
        next_ind = nums.index(target)
        indR = next_ind
        nums[next_ind] = -1
    return [indL,indR]

print(searchRange(nums,target))

# Passed
# time complexity --> O(n)
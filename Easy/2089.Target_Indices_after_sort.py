nums = [1,2,5,2,3]
target = 2

# nums = [1,2,5,2,3]
# target = 3

# nums = [1,2,5,2,3]
# target = 5
def targetIndices(nums, target):
    arr=[]
    if target not in nums:
        return arr
    nums.sort()
    while(target in nums):

        ind = nums.index(target)
        arr.append(ind)
        nums[ind] =-1
    print(arr)
targetIndices(nums,target)
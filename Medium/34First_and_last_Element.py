nums = [5,7,7,8,8,10]
target = 8
nums = [5,7,7,8,8,10]
target = 6
# nums = [1,4]
# target = 4
# nums = [3,3,3]
# target = 3
nums = []
target = 0
'''
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

Passed
time complexity --> O(n)

'''
def searchRange(nums, target):
    def search(nums,target,findFirst):
        start = 0
        end = len(nums)-1
        ans = -1
        while(start <=end):
            mid = (start+end)//2
            if nums[mid]> target:
                end = mid-1
            elif nums[mid]<target:
                start = mid+1
            else:
                ans = mid
                if findFirst:
                    end = mid -1
                else:
                    start = mid +1
        return ans
    first = search(nums,target,findFirst=True)
    last = search(nums,target,findFirst=False)
    return [first,last]

print(searchRange(nums,target))

# Passed --> O(logn)

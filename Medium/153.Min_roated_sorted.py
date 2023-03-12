nums = [3,4,5,1,2]
nums = [4,5,6,7,0,1,2]
nums = [11,13,15,17]

def find_min(nums):
    low = 0
    high = len(nums)-1
    while(low<high):
        mid = (low+high)//2
        if nums[mid]> nums[mid+1]:
            return nums[mid+1]
        if nums[mid]<nums[mid-1]:
            return nums[mid]
        if nums[mid]<nums[high]:
            high=mid-1
        if nums[mid]> nums[high]:
            low = mid+1
print(find_min(nums))
    # if high ==low:
    #     return nums[low]
    # if high<low:
    #     return nums[0]
    # mid = (low+high)//2
    # if mid<high and nums[mid]>nums[mid+1]:
    #     return nums[mid+1]
    # if mid>low and nums[mid]<nums[mid-1]:
    #     return nums[mid]
    

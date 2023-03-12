
# nums1 = [1,2]
# nums2 = [3,4]
nums1 = [1,3]
nums2 = [2]

def findMedianSortedArrays(nums1, nums2):
    nums = nums1+nums2
    nums.sort()
    ans = 0
    mid = (len(nums)//2)
    if len(nums)%2 != 0:
        ans =  (nums[mid])
    else:
        midL = mid-1
        midR = mid
        ans = (nums[midL]+nums[midR])/2
    return ans

x =findMedianSortedArrays(nums1, nums2)
print(x)

# Passed
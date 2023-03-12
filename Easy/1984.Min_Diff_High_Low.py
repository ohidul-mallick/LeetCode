

nums = [9,4,1,7]
# nums = [90]
k = 2

def minimumDifference(nums, k):
    nums.sort() # We first sort the array
    result = float('inf') # we take the result as large as possible
    left =0 # left will always be the min value in the sub array as it is sorted
    for right in range(k-1,len(nums)): # (k-1) will holds the largest value in the sub array
        #We take the minimum of (minimum so far that is result and 
        # difference between )
        result = min(result, nums[right]-nums[left]) 
        left +=1
    return result


print(minimumDifference(nums,k))
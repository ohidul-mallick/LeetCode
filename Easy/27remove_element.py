def removeElement(nums, val):
    
    l =0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[l]=nums[i]
            l+=1
    return l+1

# nums = [3,2,2,3]
# val = 3
nums = [0,1,2,2,3,0,4,2]
val =2
removeElement(nums,val)
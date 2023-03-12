def removeDuplicates(nums):
    ind =1

    for i in range(1,len(nums)):
        if nums[i-1] == nums[i]:
            pass
        else:
            nums[ind]=nums[i]
            ind +=1
    print(nums)
    print(ind)
# nums = [1,1,2]
nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)

# passed

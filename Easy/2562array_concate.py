# nums = [7,52,2,4]
nums = [5,14,13,8,12]
ans =0
while(len(nums)>0):
    if(len(nums)==1):
        ans = ans + nums[0]
        break
    else:
        first = nums.pop(0)
        last = nums.pop(-1)
        a = (str(first)+str(last))
        ans = ans + int(a)
print(ans)
# Passed
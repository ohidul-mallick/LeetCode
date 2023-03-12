# nums = [1,2,3,4]
nums = [1,1,2,3]
ans = []
for i in range(0,len(nums),2):
    freq = nums[i]
    val = nums[i+1]
    ans.extend([val for i in range(freq)])

print(ans)

# Passed

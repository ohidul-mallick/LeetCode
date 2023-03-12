# nums = [10,4,8,3]
nums = [1]
left_sum =[]
right_sum = []
left = 0
right =0
ans =[]
n = len(nums)
for i in range(n):
    
    left_sum.append(left)
    left = left + nums[i]
    right_sum.insert(0,right)
    right = right + nums[n-(i+1)]

for j in range(n):
    ans.append(abs(left_sum[j] - right_sum[j]))
print(ans)
# Passed
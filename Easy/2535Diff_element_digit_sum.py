def differenceOfSum(self, nums):
    element_sum = sum(nums)
    ans =0
    for n in nums:
        count =0
        for num in str(n):
            count = count + int(num)
        ans = ans + count
    return (abs(ans-element_sum))

# Passed

def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans =[]
        for i in range(len(nums)):
            temp = nums[i]
            ans.append(nums[temp])
        return ans

# PAssed
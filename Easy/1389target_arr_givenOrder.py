class Solution(object):
    def createTargetArray(self, nums, index):
        """
        :type nums: List[int]
        :type index: List[int]
        :rtype: List[int]
        """
        target =[]
        for i in range(len(nums)):
            ind = index[i]
            num = nums[i]
            target.insert(ind,num)
        return target
# Passed
# Beats 100% in time.
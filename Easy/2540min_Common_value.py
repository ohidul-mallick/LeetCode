def getCommon(nums1, nums2):
    st = set(nums1) & set(nums2)
    return min(st) if len(st) else -1
nums1 = [1,3]
nums2 = [2,4]
print(getCommon(nums1,nums2))

# Passed

num = 430043
k = 2
# num = 240
# k = 2
def divisorSubstrings(num: int, k: int) -> int:
    nums = str(num)
    kBeauty = 0
    
    left =0
    right = k
    while(right <= len(nums)):
        n= int(nums[left:right])
        if n>0 and num %n ==0:
            kBeauty +=1
        left +=1
        right +=1
    return kBeauty

print(divisorSubstrings(num,k))
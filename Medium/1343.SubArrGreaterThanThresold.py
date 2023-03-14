arr = [2,2,2,2,5,5,5,8]
k = 3
threshold = 4
arr = [11,13,17,23,29,31,7,5,2,3]
k = 3
threshold = 5

def numOfSubarrays(arr, k, threshold):
    left = 0
    right = k
    count =0
    sm = sum(arr[left:right])
    if sm/k >= threshold:
        count +=1
    while(right < len(arr)):
        
        sm = sm - arr[left] + arr[right]
        if sm/k >= threshold:
            count +=1
        left +=1
        right +=1
    return count

print(numOfSubarrays(arr, k, threshold))
# Passed
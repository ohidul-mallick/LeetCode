words = ["hsdqinnoha","mqhskgeqzr","zemkwvqrww","zemkwvqrww","daljcrktje","fghofclnwp","djwdworyka","cxfpybanhd","fghofclnwp","fghofclnwp"]
target = "zemkwvqrww"
startIndex = 8
def closetTarget(words, target, startIndex):
    """
    :type words: List[str]
    :type target: str
    :type startIndex: int
    :rtype: int
    """
    if target not in words:
        return -1
    right_ind = -1
    left_ind = -1
    for i in range(startIndex,len(words)):
        if words[i] == target:
            right_ind = i #4
    for j in range(startIndex):
        if words[j] == target and left_ind < j:
            left_ind = j #0
    if left_ind != -1 and right_ind != -1:
        return min(abs(left_ind - startIndex),abs(right_ind-startIndex))
    if left_ind== -1:
        left_ind = abs(startIndex + (len(words) - right_ind))
    if right_ind == -1:
        right_ind = (abs)
    return min(right_ind,left_ind)

ans = closetTarget(words, target, startIndex)
print(ans)


# Incomplete

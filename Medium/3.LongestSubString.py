"""
s = "abcabcdbb"
# s = "bbbbbbbbbbbbbbb"
s=""
s = "dvdf"

# When need to return the largest string
def lengthOfLongestSubstring(s: str) -> int:
    if len(s)==0:
        return 0
    startIndex = 0
    endIndex = -1
    largest = ""
    visited = []
    for i in range(len(s)):
        if s[i] in visited:
            endIndex = i
            temp = s[startIndex:endIndex]
            if len(temp)> len(largest):
                largest = temp
            startIndex = i
            visited = [s[i]]
        else:
            visited.append(s[i])
    return largest
print(lengthOfLongestSubstring(s))
"""


s = "abcabcbb"
# s = "bbbbbbbbbbbbbbb"
# s=" "
# s = "au"
# s = "dvdf"
# s = "aabaab!bb"
def lengthOfLongestSubstring(s: str) -> int:
    # Checking if string is empty
    if len(s)==0:
        return 0
    largest = 1 # --> It will keep track of largest string length(ans)
    visited = [] # --> In this we will kep track of all encountered distinct letters
    # Iterating over whole string
    for i in range(len(s)):
        # Checking if we already encountered the character
        if s[i] in visited:
            # If we encountered the character before ,compare the length of
            # all encountered distinct letters with largest so far.
            if len(visited)> largest:
                largest = len(visited)
            ind = visited.index(s[i])
            del visited[:ind+1]
            visited.append(s[i])
        else:
            # If character is distinct, Adding character to visited array
            visited.append(s[i])
    return max(len(visited),largest)
print(lengthOfLongestSubstring(s))

# Passed
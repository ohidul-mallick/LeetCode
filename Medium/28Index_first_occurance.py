# haystack = "sadbutsad"
# needle = "sad"
haystack = "leecodeleet"
needle = "leet"



def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    if needle not in haystack:
        return -1
    a = haystack.find(needle)
    return a

print(strStr(haystack,needle))
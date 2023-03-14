letters = ["c","f","j"]
target = "a"
letters = ["c","f","j"]
target = "c"
# letters = ["x","x","y","y"]
# target = "z"

def nextGreatestLetter(letters, target):
    start =0
    end = len(letters)-1
    while(start<=end):
        mid = (start+end)//2
        if letters[mid] > target:
            end = mid -1
        else:
            start = mid+1 # This line is doing two things -->
                            #1. if mid element is less then setting start to mid +1.
                            #2.if mid and target is equal then setting start to mid +1.
                            # It helps in getting next larger element when we found ele, when we are at last index and need to return first index(0th) as result then it increamenting last index by 1 making it equal to len of array. hence len of array modulo start will be 0(first index).

    return letters[start%(len(letters))] 


print(nextGreatestLetter(letters, target))

# Passed
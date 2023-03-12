matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 8



def arraySearch(arr,target):
    for mat in arr:
        if target in mat:
            return True
    return False

print(arraySearch(matrix,target))


# Binary Search Implementation
def findAns(arr, target):
    row = 0
    col = len(arr[row]) - 1
    while (row < len(arr) and col >= 0):
        if (arr[row][col] == target):
            return [row, col]
 
        # Target lies in further row
        if (arr[row][col] < target):
            row += 1
 
        # Target lies in previous column
        else:
            col -= 1
 
    return [-1, -1]
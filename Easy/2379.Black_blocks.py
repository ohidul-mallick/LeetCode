blocks = "WBBWWBBWBW"
k = 7
# blocks = "WBWBBBW"
# k = 2
def minimumRecolors(blocks: str, k: int) -> int:
    left = 0 # --> Left Pointer
    right = 0 # --> Right Pointer
    white_count = 0 # It will Keep track of number of white count
    smallest =float('inf') # It will keep track of smallest number of white need to recolor

    while(right< len(blocks)): # looping until right pointer reach last
        if blocks[right] == 'W': # each iteration checking how many white block we encounter
            white_count +=1
        
        if (right-left) ==(k-1): # when encountered consecutive K num of blocks
            # We take min of how many white we encounter in this and previous section
            smallest = min(smallest,white_count)

            # Now we need to update the left pointer
            #so we check if block at left is white or not
            if blocks[left] == "W":
                white_count -=1 #If white then we just decrease white by 1
            left +=1
        right +=1 # In each iteration we increament reght by 1
        # count +=1
    return smallest

print(minimumRecolors(blocks,k))
    
# Passed
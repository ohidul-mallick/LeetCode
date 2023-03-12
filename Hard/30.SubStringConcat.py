s = "barfoothefoobarman"
words = ["foo","bar"]

s = "wordgoodgoodgoodbestword"
words = ["word","good","best","word"]

# s="barfoofoobarthefoobarman"
# words =["bar","foo","the"]

# s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
# words = ["fooo","barr","wing","ding","wing"]

# s = "a"
# words = ["a"]

s = "aaaaaaaaaaaaaa"
words = ["aa","aa"]

def findSubstring(s, words):
    ln = len(words[0]) #Getting the length of sub strings
    left = 0
    right = ln
    ind =-1
    res =[]
    while(right <= len(s)): # --> Looping untill right pointer reaches end.
        temp = words.copy() # --> Creating copy to remove visited elements from list.
        currentLeft = left # --> If all words of temp is found continuously in s then 
        #currentLeft and currentRight will be left and Right 
        # otherwise Left and right will increase by only ln.
        currentRight = right
        for i in range(len(words)): # --> Looping Through temp to check 
        # all elements continuously present in s or not.
            
            word = s[currentLeft:currentRight] # Making the word
            if word in temp: # Checking if word is present in temp
                ind = left # if present then we have found possible ans Index
                temp.remove(word) # we remove the found element
                currentLeft +=ln # increament by ln
                currentRight +=ln
            else:
                break # if element not present in temp then break
        # length of temp will be 0 if we found all elements of temp continuous order in s.
        if len(temp)==0:
            res.append(ind) #That means ind, which was our possible ans is our actual ans.
            # increament left and right by currentLeft and right.
            left = ind+1
            right = left+ln
        else:
        # Otherwise we increase left and right by ln.
            left +=1
            right +=1
    return res
            
print(findSubstring(s, words))

# Passed
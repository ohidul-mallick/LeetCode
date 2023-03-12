# words = ["gin"]
# words = ["gin","zen","gig","msg"]
words =["mevzi","mevzi","gvgs","qhiwg","qhijn","b","b","b","b","b"]

def uniqueMorseRepresentations(words):
    code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
    if len(words) ==1:
        return 1
    arr = set()
    for word in words:
        s = ''
        for w in word:
            value = ord(w) - 97
            s+=code[value]
        arr.add(s)
    print(arr)

uniqueMorseRepresentations(words)


# Passed
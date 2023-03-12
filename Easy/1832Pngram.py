def checkIfPangram(sentence):
    if len(sentence)<26:
        return False
    letters = "abcdefghijklmnopqrstuvwxyz"
    letter =[]
    letter[:0] = letters
    count = True
    for l in letter:
        if l not in sentence:
            count = False
    return count
s = "thequickbrownfoxjumpsoverthelazydog"
print(checkIfPangram(s))

# Passed
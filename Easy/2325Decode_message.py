key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"

def decodeMessage(key, message):
    i = 97
    ans = ""
    letter = {}
    for k in key:
        if k in letter or k == " ":
            pass
        else:
            letter[k] = chr(i)
            i+=1
    for m in message:
        if m == " ":
            ans = ans + " "
        else:
            ans = ans + letter.get(m)
    print(ans)

decodeMessage(key,message)

# Passed
# Important
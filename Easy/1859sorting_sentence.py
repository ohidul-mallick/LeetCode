s = "is2 sentence4 This1 a3"
a = s.split()
# ans =[0]*len(a)
# res =" "
# for sentence in a:
#     num = int(sentence[-1])
#     sentence = sentence.replace(sentence[-1],'')
#     ans[num-1]=sentence
# print(res.join(ans))

# Passed

# -------------
a.sort(key =lambda a :(a[-1]))
z = " ".join(w[:-1] for w in a)
print(z)


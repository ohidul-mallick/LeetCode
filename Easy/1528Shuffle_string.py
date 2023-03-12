s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
ans =[0]*len(indices)
a = ""
for i in range(len(s)):
    ans[indices[i]] = s[i]

print(a.join(ans))
# Passed
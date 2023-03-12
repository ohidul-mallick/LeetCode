# s = "A1:F1"
# s = "K1:L2"
s = "U7:X9"
first = ord(s[0])
last = ord(s[3])
num2 = int(s[4])+1
num1 = int(s[1])
ans = []
for i in range(first,(last+1)):
    letter = chr(i)

    for j in range(num1,num2):
        cell = letter + str(j)
        ans.append(cell)
print(ans)
# Passed

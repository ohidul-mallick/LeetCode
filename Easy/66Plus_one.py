def plusOne(digits):
    
    s = ''.join(str(digit) for digit in digits )
    temp = int(s)+1
    s= str(temp)
    digits = [int(x) for x in s]
    return digits
digits = [1,2,3]
print(plusOne(digits))

# Passed
# Passed
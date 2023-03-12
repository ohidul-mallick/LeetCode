# arr = [1,4,2,5,3]
# arr = [1,2]
# arr = [10,11,12]
arr = [1]
a = sum(arr)
res = []
for i in range(3,len(arr),2):
    j = i
    k =0
    while((k+i)<=len(arr)):
        b = sum(arr[k:j])
        k +=1
        j +=1
        res.append(b)
if len(arr) %2 != 0 and len(arr) != 1:
    res.append(a)
res.append(a)
print(sum(res))
# take first 3 --> get sum 

# Passed
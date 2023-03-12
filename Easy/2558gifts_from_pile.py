import math
# gifts = [25,64,9,4,100]
gifts = [1,1,1,1]
k = 4

while(k>0):
    mx = max(gifts)
    sqre_root = math.floor(math.sqrt(mx))
    ind = gifts.index(mx)
    gifts = gifts[:ind]+[sqre_root]+gifts[ind+1:]
    k=k-1
print(sum(gifts))
# Passed
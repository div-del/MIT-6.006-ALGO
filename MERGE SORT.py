L = [8,4,5,1,6]
L1 = []
L2 = []
L3 = []
for i in range(0,3):
    L1 += [L[i],]
    L1 = sorted(L1)
print(L1)
for j in range(3,5):
    L2 += [L[j],]
    L2 = sorted(L2)
print(L2)
max1 = 0
for i in L1:
    for j in L2:
        if i<j and i not in L3:
            L3 += [i,]
            max1 = j
        elif j not in L3:
            L3 += [j,]
            max1 = i
        else:
            continue
L3 += [max1,]
print(L3)

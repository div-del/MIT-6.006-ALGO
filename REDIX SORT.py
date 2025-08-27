L = []
L1 = []
L2 = []
L3 = []

n=int(input("enter the size of list "))
for i in range(n):
    k=int(input("enter element "))
    L+=[k,]
    
#####sort by one's
    
D={}
for i in L:
    o=i%10
    if o in D:
        D[o].append(i)
    else:
        D[o]=[i,]

K=sorted(D)
print(D)

for i in K:
    L1+=D[i]

print(L1)
##########sort by ten's
D={}
for i in L1:
    o=(i//10)%10
    if o in D:
        D[o].append(i)
    else:
        D[o]=[i,]

K=sorted(D)
print(D)
for i in K:
    L2+=D[i]

print(L2)

##########sort by hundreds
D={}
for i in L2:
    o=i//100
    if o in D:
        D[o].append(i)
    else:
        D[o]=[i,]

K=sorted(D)
print(D)
for i in K:
    L3+=D[i]

print(L3)

def merge_sort(L):
   
   L1 = []
   L2 = []
   L3 = []
   if len(L)%2!=0:
       k=(len(L)+1)/2
   else:
       k=len(L)/2
   for i in range(0,k):
     L1 += [L[i],]
     L1 = sorted(L1)
   print(L1)
   for j in range(k,len(L)):
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

L = [8,4,5,1,9]
merge_sort(L)
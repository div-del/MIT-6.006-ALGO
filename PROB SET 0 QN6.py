def count_incsub(A):
    count={}
    k=0
    L=()
    L+=(A[0],)
    t=0
    for i in range (1,len(A)):
       
        if A[i]>A[i-1]:
            L+=(A[i],)
        else:
            print(L)
            
            if len(L) in count:
                count[len(L)]+=1
            else:
                count[len(L)]=1
            
            
            L=(A[i],)
            
            k+=1
    print(L)
    count[len(L)]=1
    print(count)
    K=count.keys()
    M=max(K)
    sub=count[M]
    print("no. of inc subarrays ",sub)
        
    
A=()
n=int(input("enter size of tuple "))
for i in range(n):
    k=int(input("enter element "))
    A+=(k,)
count_incsub(A)  

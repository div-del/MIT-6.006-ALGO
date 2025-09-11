A=int(input("enter the amount "))

C=[1,5,6,8]



dp=[A+1]*(A+1)
dp[0]=0
def coin_change(A,C):
    for i in range(1,A+1):
        
        for c in C:
            if i-c>0:
                dp[i]=min(dp[i],dp[i-c]+1)
            elif i-c==0:
                dp[i]=1
    if dp[A]>A:
        return -1
    else:
        print(dp)
        return dp[A]
coin_change(A,C)
        



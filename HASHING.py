T=[]
for i in range (10):
    T+=[[],]
    
m=10
def insert():
    value=input("enter value to input ")
    k=int(input("enter a key "))
    i=k%m
    T[i]+=[[k,value],]
    print("insert successful")
    print(T)
    print()
def find():
    k=int(input("enter key of value to find "))
    i=k%m
    
    found=0
    for j in range(len(T[i])):
        if T[i][j][0]==k:
            found=1
            value=T[i][j][1]
    if found==0:
        print("key not found darling")
    else:     
        print("the value having key ",k," is ",value)
    print()
while True:
    print("1. insert")
    print("2. find")
    print("3. stop")
    ch=int(input("enter choice "))
    if ch==1:
        insert()
    if ch==2:
        find()
    if ch==3:
        break

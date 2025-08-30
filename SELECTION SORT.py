l = [8, 2, 4, 9, 3]
min_l = l[0]
k = 0
key = 0
def check():
    global k
    global min_l
    min_l = l[k]
    for i in range(k, len(l)):
        if l[i] <= min_l:
            min_l = l[i]
            key = i
    return key
while k <= (len(l)-1):
    key = check()
    l[k], l[key] = l[key], l[k]
    print(l)
    k += 1
print(l)

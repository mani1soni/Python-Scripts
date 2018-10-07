def GoodString(a):
    n = 0
    i = 0
    while(i < len(a)):
        j = i+1
        while(j < len(a)):
            if(a[j] == a[i]):
                a.pop(j)
                n = n+1
            else:
                j = j+1
        i = i+1
    return n


a = input()
a = list(a)
q = GoodString(a)
print(q)
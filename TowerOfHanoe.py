#program to find steps for tower of hanoe for n discs

def tower(n,a,b,c):
    print(a,b,c)
    if n==1:
        print("move disk %s from %s to %s"%(n,a,c))
        return
    else:
        tower(n-1,a,c,b)
        print("move disk %s from %s to %s"%(n,a,c))
        #print(a,b,c)
        tower(n-1,b,a,c)
        #no of discs
num=int(input("enter the number of disks"))
#three pegs with name as
a="source"
b="auxilary"
c="target"
tower(num,a,b,c)
print(a,b,c)

def ls(a,key):
    n=len(a)
    for i in range(n):
        if a[i]==key:
            return i;
    return -1
aa=[1,34,5535,334,44,344,4]
bb=int(input("enter key "))
d=ls(aa,bb)
if d==-1:
    print('element not found')
else:
    print("found",d)

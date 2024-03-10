def bs(a):
    b=len(a)
    for i in range(b-1):
        for j in range(b-1-i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
            print(a)
        print("\n"*1)


list=[4,2,7,4,1,9,6,3]
bs(list)



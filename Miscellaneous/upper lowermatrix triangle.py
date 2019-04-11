while True:
    m=input("Rows:")
    n=input("Columns:")
    L=[]
    for i in range(m):
        l=[]
        for j in range(n):
            x=input('Element:')
            l.append(x)
        L.append(l)
    for l in L:
        for x in l:
            print x,
        print
    print"Upper Matrix is:"
    for i in range(m):
        for j in range(n-i):
            print L[i][j],
        print
    print"Lower Matrix is:"
    for i in range(m):
        print '  '*(m-i-1),
        for j in range(n-1-i,n):
            print L[i][j],
        print
    

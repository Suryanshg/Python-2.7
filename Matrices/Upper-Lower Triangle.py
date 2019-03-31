while True:
    L=[]
    m=int(input("Rows:"))
    n=int(input("Columns:"))
    for i in range(m):
        l=[]
        for j in range(n):
            x=int(input("Elements:"))
            l.append(x)
        L.append(l)
    for l in L:
        for x in l:
            print x,
        print
    print"Upper Triangle is:"
    for i in range(m):
        for j in range(n-i):
            print L[i][j],
        print
    print"Lower Triangle is:"
    for i in range(m):
        print "  "*(m-1-i),
        for j in range(n-1-i,n):
            print L[i][j],
        print
            
    

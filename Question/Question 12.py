while True:
    L=[]
    m=int(input("Rows:"))
    n=int(input("Columns:"))
    for i in range(m):
        l=[]
        sr=0
        for j in range(n):
            x=int(input("Element:"))
            l.append(x)
            sr+=x
        l.append(sr)
        L.append(l)
    l=[]
    for i in range(m):
        sc=0
        for j in range(n):
            sc+=L[j][i]
        l.append(sc)
    L.append(l)       
    
    for l in L:
        for x in l:
            print x,
        print
    
            

while True:
    L=[]
    m=int(input("Rows:"))
    n=int(input("Columns:")) 
    for i in range(m):
        l=[]
        for j in range(n):
            x=int(input("Element:"))
            l.append(x)
        L.append(l)
    
    for l in L:
        for x in l:
            print x,
        print
    trmatrix=[]
    for i in range(n):
        l=[]
        for j in range(m):
            l.append(L[j][i])
        trmatrix.append(l)
    for l in trmatrix:
        for x in l:
            print x,
        print

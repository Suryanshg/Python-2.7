while True:
    m=int(input("Rows for Matrix 1:"))
    n=int(input("Columns for Matrix 1:"))
    p=int(input("Rows for Matrix 2:"))
    q=int(input("Columns for Matrix 2:"))
    L1=[]
    for i in range(m):
        l=[]
        for j in range(n):
            x=int(input("Enter Element for Matrix 1:"))
            l.append(x)
        L1.append(l)
    print "Matrix 1 is:"
    for l in L1:
        for x in l:
            print x,
        print
    L2=[]
    for i in range(p):
        l=[]
        for j in range(q):
            y=int(input("Enter Element for Matrix 2:"))
            l.append(y)
        L2.append(l)
    print "Matrix 2 is:"
    for l in L2:
        for y in l:
            print y,
        print
    if ((m==p) and (n==q)):
        L3=[]
        print "Resultant Matrix is:"
        for i in range(m):
            l=[]
            for j in range(n):
                x=L1[i][j]+L2[i][j]
                l.append(x)
            L3.append(l)
        for l in L3:
            for x in l:
                print x,
            print
    else:
        print "Both the Matrices should have the same dimensions.Addition is not possible."
            
                
        
            
            

while True:
    L1=[]
    L2=[]
    L3=[]
    m=int(input("Enter the number of rows for Matrix 1:"))
    n=int(input("Enter the number of columns for Matrix 1:"))
    print
    p=int(input("Enter the number of rows for Matrix 2:"))
    q=int(input("Enter the number of columns for Matrix 2:"))
    for i in range(m):
        l=[]
        for j in range(n):
            x=int(input("Enter the element for Matrix 1:"))
            l.append(x)
        L1.append(l)
    print "Matrix 1 is:"
    for l in L1:
        for x in l:
            print x,
        print
    for i in range(p):
        l=[]
        for j in range(q):
            y=int(input("Enter the element for Matrix 2:"))
            l.append(y)
        L2.append(l)
    print "Matrix 2 is:"
    for l in L2:
        for y in l:
            print y,
        print
    if (n==p):
        for i in range(m):
            l3=[]
            for j in range(q):
                l=0
                for k in range(n):
                    l=l+L1[i][k]*L2[k][j]
                l3.append(l)
            L3.append(l3)
        print "Resultant Matrix is:"
        for l in L3:
             for y in l:
                 print y,
             print
    else:
        print "Sorry Multiplication is not possible because columns of Matrix 1 should be equal to rows of Matrix 2."
                    
                    
    
                
                    
                    
            
    
    
        
    

m=int(input("Rows:"))
n=int(input("Columns:"))
L=[]
if m==n:
    for i in range(m):
        l=[]
        for j in range(n):
            x=int(input("Element:"))
            l.append(x)
        L.append(l)
    print "First diagonal is:"
    for i in range(m):
        print " "*i,L[i][i]
    print "Second diagonal is:"
    for i in range(m):
        print " "*(n-1-i),L[i][n-1-i]
else:
    print "Sorry diagonals exist for only square matrix."
        
        

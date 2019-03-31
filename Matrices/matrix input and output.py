while True:
    L=[]
    
    m=int(input("Enter the number of rows:"))
    n=int(input("Enter the number of columns:"))
    for i in range(m):
        l=[]
        for j in range(n):
            x=int(input("Enter the element:"))
            l.append(x)
        L.append(l)
    
    for l in L:
        for x in l:
            print x,
            
        print
        
          

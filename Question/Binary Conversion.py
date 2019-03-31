while True:
    try:
        x=int(input("Enter a number:"))
        L=[]
        if x==0:
            print x
        else:
            while x!=0:
                r=x%2
                x=x/2
                L.append(r)
            L.reverse()
            for i in L:
                print i,
            print
    except:
        print "Error"
                
               

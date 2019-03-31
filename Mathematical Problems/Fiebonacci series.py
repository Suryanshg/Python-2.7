while True:
    a=0
    b=1
    l=int(input("Enter the Fiebonacci Limit:"))
    print a
    print b
    
    for i in range(3,l+1,1):
        c=a+b
        print c
        a=b
        b=c
     


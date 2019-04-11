while True:
    n=int(input("Enter the number of elements:"))
    L=[]
    for i in range(n):
        x=input("Enter the Elements:")
        L.append(x)
    print L
    a=input("Enter the Element to search:")
    l=0
    for i in range(n):
        if(L[i]==a):
            l+=1
            print "Got it! It's at",i,"index."
    if(l==0):
        print "Sorry, it's not in the List."
    else:
        print
        
        
        
    

while True:
    L=input("Enter the elements in the list, separated by commas:")
    print L
    l=[]
    for i in range(len(L)):
         for x in L:
            flag=0
            for y in L:
                if (x>=y):
                    flag+=1
            if (flag==len(L)-i):
                l.append(x)
    print "The sorted list in descending order is:",l
                

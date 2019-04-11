import pickle
import re
with open("log.dat","wb") as mf:
    n=int(input("Enter the number of records:"))
    L=[]
    for i in range(n):
        x=raw_input("Enter the string:")
        L.append(x)
    pickle.dump(L,mf)
    print "L:",L
with open("log.dat","rb") as mf:
    A=pickle.load(mf)
    print "A:",A
    count=0
    tot=0
    comp=re.compile("Xerror:(0.[0-9]*)")
    for i in A:
        obj=comp.search(i)
        if obj:
            count+=1
            tot+=float(obj.group(1))
    print "Total",tot
    print "Count",count
        
        
        

    
    
        
    
    

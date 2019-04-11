L=input("Enter the list within []:")
ch=raw_input("Enter your choice: Ascending(A)/Descending(D):")
if ch.upper()=="A":
    for i in range(len(L)):
        for j in range(len(L)-i-1):
            if L[j]>L[j+1]:
                L[j+1],L[j]=L[j],L[j+1]
    print L
elif ch.upper()=="D":
     for i in range(len(L)):
        for j in range(len(L)-i-1):
            if L[j]<L[j+1]:
                L[j+1],L[j]=L[j],L[j+1]
     print L
    

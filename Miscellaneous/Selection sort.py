L=input("Enter list within [ ]:")
ch=raw_input("Enter your choice: Ascending(A)/Descending(D):")
if ch.upper()=="A":
    for i in range(len(L)):
        for j in range(i,len(L)):
            if L[j]<L[i]:
                L[i],L[j]=L[j],L[i]
    print L
elif ch.upper()=="D":
    for i in range(len(L)):
        for j in range(i,len(L)):
            if L[j]>L[i]:
                L[i],L[j]=L[j],L[i]
    print L

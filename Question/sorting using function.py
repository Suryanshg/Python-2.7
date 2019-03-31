while True:
    def sort(L,c):
        for i in range(len(L)):
            ma=L[i]
            for j in range(i+1,len(L)):
                if (L[i]<L[j]):
                    ma=L[j]
                    L[j]=L[i]
                    L[i]=ma
        if (c=='d'):
            print L
        else:
            L.reverse()
            print L
    L=input("Enter a List:")
    c=raw_input("Enter 'a' for ascending and 'd' for descending:")
    sort(L,c)


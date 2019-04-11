def sort(L,ch):
    M=[]
    while len(L)!=0:
        M.append(min(L))
        L.remove(min(L))
    if ch=="D" or ch=="d":
        M.reverse()
        return M
    elif ch=="A" or ch=="a":
        return M
L=input("Enter List to be sorted within []:")
ch=raw_input("Enter A for Ascending and D for Descending:")
result=sort(L,ch)
print result

        

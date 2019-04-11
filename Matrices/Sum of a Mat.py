L=[]
m=int(input("Rows:"))
n=int(input("Columns:"))
for i in range(m):
    l=[]
    for j in range(n):
        x=int(input("Element:"))
        l.append(x)
    L.append(l)
s=0
for l in L:
    for x in l:
        s+=x
print "The sum of elements of a matrix is:",s


    

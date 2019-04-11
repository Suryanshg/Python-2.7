L=[]
n=int(input("Enter the number of elements:"))
for i in range(n):
    x=int(input("Enter the elements of the list:"))
    L.append(x)
x=int(input("Enter the target element:"))
ub=len(L)-1
lb=0
flag=0
while ub!=lb and flag==0:
    mid=(ub+lb)/2
    if x==L[mid]:
        flag=1
    elif x<L[mid]:
        ub=mid-1
    else:
        lb=mid+1
if flag==1:
    print "Found!"
else:
    print "Not Found!"

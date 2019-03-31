while True:
 a=raw_input("Enter Your Name:")
 b=len(a)
 j=0
 flag=0
 for i in range(b-1,-1,-1):
    print a[i],
    if (a[i]!=a[j]):
        flag=1
    j=j+1    
 if (flag==0):
    print "is a palindrome"
 else:
    print "is not a palindrome"

 
  
 
    
 

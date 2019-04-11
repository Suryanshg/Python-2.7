a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
e=(b**2)-(4*a*c)
d=e**(1/2)
if e<0:
    print "Error, This will result in a complex root."
elif a==0:
    print "This isn't a quadratic equation."
else:
    r1=(-b+d)/(2*a)
    r2=(-b-d)/(2*a)
    print "Root 1 =",r1
    print "Root 2 =",r2

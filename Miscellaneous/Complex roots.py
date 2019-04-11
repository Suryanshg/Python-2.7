while True:
    a=int(input("Enter the coefficient of x^2:"))
    b=int(input("Enter the coefficient of x:"))
    c=int(input("Enter the constant:"))
    b=pow(b,2)
    d=(b)-(4*a*c)
    if a!=0:
        if d>=0:
            d=pow(d,1.0/2.0)
            x=(-b+d)/(2*a)
            y=(-b-d)/(2*a)
            print x,y, "are the roots of the given quadratic equation."
        else:
            print "The roots are complex in nature."
            d=d*-1
            x=complex(-b/2*a,(pow(d,0.5))/(2*a))
            y=complex(-b/2*a,-1*(pow(d,0.5))/(2*a))
            print x,y, "are the roots of the given quadratic equation."
    else:
        print "This is not a quadratic equation."

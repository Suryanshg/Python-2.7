def generatefib(n):
    x,y=0,1
    while x<=n:
        yield x
        x,y=y,x+y
n=int(input("Enter the limit of Fibonacci series:"))
L=list(generatefib(n))
print L

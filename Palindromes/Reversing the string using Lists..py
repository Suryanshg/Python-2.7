while True:
    name=raw_input("Enter any string:")
    list1=list(name)
    a=list(name)
    list2=list1.reverse()
    if (a==list1):
        print "Its a Palindrome"
    else:
        print "Not a palindrome"

while True:
    usrnm=raw_input("Enter the Username:")
    pswrd=raw_input("""Criterion for Password setting:
1. Minimum length should be 6
2. Maximum length should be 10
3. Should be a combination of alphabets and digits,
Enter the Password: """)
    if (len(pswrd)<=10 and len(pswrd)>=6):
        if pswrd.isalnum()==True:
            print "Valid Password"
        else:
            print "Invalid Password"
    else:
        print "Invalid Password"
        

    
    

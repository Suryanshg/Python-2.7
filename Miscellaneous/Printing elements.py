while True:
    L=input("Enter the list:")
    for i in L:
        if i.isdigit()==True:
            print i*3
        else:
            print i+"#"

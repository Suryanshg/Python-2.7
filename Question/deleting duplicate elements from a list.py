while True:
     L=input("Enter the elements in a List:")
     for i in L:
          if i in L[L.index(i)+1:]:
               L.remove(i)
     print L
     print "Got it!"



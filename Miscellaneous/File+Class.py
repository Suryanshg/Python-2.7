import pickle
class STUDENT:
        def __init__(self):
            self.RNO=0
            self.NAME=""
            self.STREAM=""
            self.PERCENT=0.0
        def ACCEPT(self):
            self.RNO=input("Enter Roll no:")
            self.NAME=raw_input("Enter Name:")
            self.STREAM=raw_input("Enter Stream:")
            self.PERCENT=input("Enter Percentage:")
        def DISPLAY(self):
            print self.RNO,self.NAME,self.STREAM,self.PERCENT
        def RET_STREAM(self):
            return(self.STREAM)
n=int(input("Enter the number of records:"))
L=[]
for i in range(n):
        O=STUDENT()
        O.ACCEPT()
        L.append(O)
with open("Student.dat","wb") as mf:
    pickle.dump(L,mf)
with open("Student.dat","rb") as mf:
    x=pickle.load(mf)
for record in x:
    if(record.RET_STREAM()=="HUMANITIES"):
        record.DISPLAY()
                
            
    


        

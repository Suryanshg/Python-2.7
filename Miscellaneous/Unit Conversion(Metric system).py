while True:
    units={'mm':0.001,'cm':0.01,'dm':0.1,'m':1.0,'dam':10.0,'hm':100.0,'km':1000.0}
    def convertfrom(sunit,tunit,mag):
        return mag*(units[sunit])/(units[tunit])
    
    sunit=raw_input("Enter the Source Unit:")
    tunit=raw_input("Enter the Target Unit:")
    mag=int(input("Enter the Magbitude:"))
    x=convertfrom(sunit,tunit,mag)
    print x,tunit

while True:
    date=raw_input("Enter the date in the ddmmyy format:")
    cent=int(input("Enter the century:"))
    day=date[0:2:1]
    month=date[2:4:1]
    year=str(cent-1)+date[4:6:1]
    if ((int(day)<=31) and (int(month)<=12)):
        months={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October',
            '11':'November','12':'December'}
        sup={'01':'st','02':'nd','03':'rd','04':'th','05':'th','06':'th','07':'th','08':'th','09':'th','10':'th','11':'th','12':'th','13':'th','14':'th'
         ,'15':'th','16':'th','17':'th','18':'th','19':'th','20':'th','21':'st','22':'nd','23':'rd','24':'th','25':'th','26':'th','27':'th','28':'th'
         ,'29':'th','30':'th','31':'st'}
        print day+sup[day],months[month],year
    else:
        print "Invalid Input! Please try again."
    
    
            
    


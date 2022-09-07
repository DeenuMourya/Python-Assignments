#python script to print days in month according to number pressed

mon=int(input("Enter the number of month : "))

if mon==1:
    print('January , 31 days')
elif mon==2:
    print('February , 28 days')
elif mon==3:
    print('March , 31 days ')
elif mon==4:
    print("April , 30 days ")
elif mon==5:
    print("May , 31 days ")
elif mon==6:
    print('June , 30 days ')
elif mon==7:
    print('July , 31 days ')
elif mon==8:
    print('August , 31 days ')
elif mon==9:
   print('September , 30 days')
elif mon==10:
   print('October , 31 days')
elif mon==11:
    print('November , 30 days ')
elif mon==12:
    print('December , 31 days')
else:
    print('Invalid key pressed  :  ')
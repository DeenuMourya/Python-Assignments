#python script to display number of days in month 

mon=int(input('Enter month number : '))

match mon:
    case 1:
        print('January , 31 days ')
    case 2:
        print('February , 28 days ')
    case 3: 
        print('March , 31 days ')
    case 4:
        print("April , 30 days")
    case 5: 
        print("May , 31 days")
    case 6:
        print("June , 30 days ")
    case 7:
        print("July , 31 days ")
    case 8:
        print("August , 31 days")
    case 9:
        print("September , 30 days")
    case 10:
        print("October , 31 days")
    case 11:
        print('November , 30 days')
    case 12: 
        print('December , 31 days')
    case _:
        print("Invalid month number entered")
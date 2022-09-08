#python script to check year type

yr=int(input('Enter an year'))

match yr%100==0:
    case 1:
        print('Centuary leap year') if yr%400==0 else print('Centuary non leap year ')
    case 0:
        print('Non Centuary Leap year') if yr%4==0 else print('Non Centuary non leap year')
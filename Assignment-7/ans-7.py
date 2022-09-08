#python script to check whether a number is +ve , -ve or 0

num=eval(input('Enter an number '))

match num:
    case num if num>0:
        print("Number is positive")
    case num if num<0:
        print('Number is negative')
    case num if num==0:
        print('Number is zero')

#python script to do calculations via menu driven program

a=eval(input('Enter Number 1 : '))
b=eval(input('Enter Number 2 : '))

op=input("Press operator according to their operations from list : '+,-,/,*' ::::: ")

match op:
    case '+':
        print("The sum of the numbers is",a+b)
    case '-':
        print("The difference of numbers is",a-b)
    case '*':
        print("The product of the numbers is",a*b)
    case '/':
        print("The division of the numbers is",a/b)
    case _:
        print("Invalid key pressed")
#python script to check triangle type

print("Select option to check type of triangle :::")
print('1. For Isosceles triangle','2. For Right angled triangle','3. For Equilateral triangle','4. Exit',sep='\n')

op=int(input())

if (op>4 or op<1):
    print('invalid choice')
    exit()
elif op==4:
    print("Exit pressed")
    exit()
    
print('To check Enter the sides of the triangle : ')

a=eval(input('Enter side 1 of Triangle : '))
b=eval(input('Enter side 2 of Triangle : '))
c=eval(input('Enter side 3 of Triangle : '))

if (a<b+c or b>a+c or c>a+b):
    print("Triangle is valid :")
else:
    print("Triangle is not valid :")


match op:
    case 1:
        if ((a==b or b==c or c==a) and ( not a==b==c) ):
            print('Isosceles Triangle')
        else:
            print("Not Isosceles Triangle")
    case 2:
        if ( a*a==b*b+c*c or b*b==a*a+c*c or c*c==a*a+b*b ):
            print("Right angled Triangle")
        else:
            print("Not Right angled Triangle")
    case 3:
        a=b=c if print('Equilateral Triangle') else print("Not Equilateral Triangle")


        


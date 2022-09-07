#python script to Check type of roots of equation

print('Enter quadratic equation in parts')
a=eval(input("Enter value of a = "))
b=eval(input("Enter value of b = "))
c=eval(input("Enter value of c = "))
print('\nYour entered equation is %dx^2+%dx+%d '%(a,b,c))

if b**2-(4*a*c)>0:
    print("Real roots")
elif b**2-(4*a*c)==0:
    print('Real and equal roots')
else:
    print("Imaginary roots")

#python script to find greatest number among 3 numbers

num1=int(input('Enter number 1: '))
num2=int(input('Enter number 2: '))
num3=int(input('Enter number 3: '))

if num1>num2>num3:
    print('Greatest number is :',num1)
elif num2>num3:
    print("Greatest number is :",num2)
else:
    print("Greatest number is :",num3)
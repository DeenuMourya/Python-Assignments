#python script to swap two numbers 

a=int(input("Enter number 1= "))
b=int(input("Enter number 2= "))
print("Before swap a = ",a,'b = ',b)

a=a+b
b=a-b
a=a-b
print('After swap a = ',a,"b = ",b)
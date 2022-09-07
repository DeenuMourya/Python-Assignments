#python script to take complex number from the user and find greater between imaginary and real part

print("Enter an complex number in parts :")
real=int(input("Enter real part : "))
img=int(input("Enter imaginary part : "))
complex=complex(real=real,imag=img)
print(complex)

if real>img:
    print("Real part is greater :",real)
else:
    print("Imaginary part is greater :",img)
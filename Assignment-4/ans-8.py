#python script to calculate simple interest

amount=int(input("Enter the amount "))
time=int(input("Enter the time in years "))
rate=float(input("Enter the rate "))

print("The simple interest is ",(amount*rate*time)/100)
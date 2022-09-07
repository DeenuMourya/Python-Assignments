#python script to check leap year

yr=int(input("Enter  a year  "))

if yr%100==0:
    if yr%400==0:
        print("It is a leap year")
    else:
        print("It is not an leap year")
elif yr%4==0:
    print("It is a leap year ")
else:
    print("It is not an leap year")

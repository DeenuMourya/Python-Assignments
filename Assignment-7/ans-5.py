#pyhton script to take input from user and output according to index

n=int(input('Enter an number: '))

match n:
    case n if n%2==0:
        print('Saurabh Shukla')
    case n if n%2!=0 and n<0:
        print("Prateek Jain")
    case n if n%2!=0 and n>0:
        print("Aditya Chaudary")
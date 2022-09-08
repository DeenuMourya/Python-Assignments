#python script to check string is multiword or not

a=input('Enter an string ::: ')

match a:
    case a if ' 'in a:
        print('It is a multiword string')
    case _:
        print('It is single word string')
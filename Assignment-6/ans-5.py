#python script to print two words in dictionary order

w1=input("Enter 1st word ")
w2=input('Enter 2nd word ')

print('words in sorted dictionary order')
if w1<w2:
    print(w1,w2,sep='\n')
else:
    print(w2,w1,sep='\n')
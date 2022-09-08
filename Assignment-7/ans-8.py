#python script to compare two strings in dictionary order

s1=input('Enter string 1 : ')
s2=input('Enter string 2 : ')

match s1:
    case s1 if s1==s2:
        print("Strings are identical")
    case s1 if s1<s2:
        print(s1,'is greater in dictionary order than',s2)
    case s1 if s2<s1:
        print(s2,'is greater in dictionary order than',s1)


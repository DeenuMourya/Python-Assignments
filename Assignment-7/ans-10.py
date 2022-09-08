#python script to print day according to respected colour name

color=input('Enter your favourite colour,input like "i like ___ colour" or can directly write name of color:: ')

match color:
    case color if 'yellow'in color:
        print('Monday')
    case color if 'blue'in color:
        print('Tuesday')
    case color if 'orange'in color:
        print('Wednesday')
    case color if 'white'in color:
        print('Thrusday')
    case color if 'black'in color:
        print('Friday')
    case color if 'red'in color:
        print('Saturday')
    case _:
        print('Sunday')
    

def distance(x1, y1, x2, y2):
    return (abs(x1-x2)**2 + abs(y1-y2)**2)**0.5

def pointDistCal():
    x1 = float(input('Enter x cordinates of the first point - '))
    y1 = float(input('Enter y cordinates of the first point - '))
    x2 = float(input('Enter x cordinates of the second point - '))
    y2 = float(input('Enter y cordinates of the second point - '))

    print(f'Distance between the two points is {distance(x1, y1, x2, y2)} units')

pointDistCal()

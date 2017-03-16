x1 = int(input())
y1 = int(input())

x2 = int(input())
y2 = int(input())

x3 = int(input())
y3 = int(input())

side1 = ((x1 - x2)**2 )+ ((y1-y2)**2)
side2 = ((x2 - x3)**2 )+ ((y2-y3)**2)
side3 = ((x1 - x3)**2 )+ ((y1-y3)**2)

if True:
    a = side1+side2 == side3 or side2+side3 == side1 or side1+side3 == side2
    print (' Это прямоугольный треугольник')
else:
    print ('Это не прямоугольный треугольник')
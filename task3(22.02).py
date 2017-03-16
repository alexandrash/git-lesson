print ('Введите х и у:')
x = int(input())
y = int(input())


def quarter(x, y):
    if x > 0 and y > 0:
        return 2
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y < 0:
        return 4

print (quarter(x,y))

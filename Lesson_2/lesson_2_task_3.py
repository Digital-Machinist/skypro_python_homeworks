import math
side = input("Введите сторону квадрата:")
side = float(side)
def square():
    if side % 1 == 0:
        return side * side
    else:
        square = math.ceil (side * side)
        return square
print('Площадь квадрата равна:', int(square()))

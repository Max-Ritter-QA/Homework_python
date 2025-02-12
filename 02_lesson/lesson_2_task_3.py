import math

def square(a):
    return math.ceil(a * 2)
a = float(input("Введите длину стороны: "))
print("Площадь квадрата =", square(a))

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Enter coordinate X: '))
y = int(input('Enter coordinate Y: '))
if x==0 or y==0:
    print('Error')
elif x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
elif x < 0:
    if y > 0:
        print(2)
    else:
        print(3)
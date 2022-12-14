# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
quarter_num = int(input('Input quarter number: '))
if quarter_num > 4 or quarter_num < 1:
    print('Error')
elif quarter_num == 1:
    print('x > 0 and y > 0')
elif quarter_num == 2:
    print('x < 0 and y > 0')
elif quarter_num == 3:
    print('x < 0 and y < 0')
elif quarter_num == 4:
    print('x > 0 and y < 0')

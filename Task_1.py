#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.


day = int(input('Input number of day week: '))
if day == 6 or day == 7:
    print('This day is a weekend')
elif day > 7 or day < 1:
    print('Error!')
else:
    print('This day is not a weekend')

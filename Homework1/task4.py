# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
# Пример:
# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти


quarter = int(input('Введите номер четверти: '))
if quarter == 1:
    print('Диапазон точек в этой четверти: x > 0, y > 0')
if quarter == 2:
    print('Диапазон точек в этой четверти: x < 0, y > 0')
if quarter == 3:
    print('Диапазон точек в этой четверти: x < 0, y < 0')
if quarter == 4:
    print('Диапазон точек в этой четверти: x > 0, y < 0')
if quarter > 4 or quarter < 1:
    print('Нет такой четверти')

# Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

print('Введите количество вещественных цифр в списке: ')
n = int(input())

from random import uniform

if n <= 0:
    print('Введите число > 0')
else:
    list = []                              
    for i in range(n):
        list.append(round(uniform(1, n), 2))
    print(list)

    max = min = round(list[0] % 1, 2)
    result = 0
    i = 1
    for i in range(len(list)):
        num = round(list[i] % 1, 2)
        if num > max:
            max = num
        if num < min:
            min = num
    result = round((max - min), 2)
    print('Min: ', min, ' Max: ', max,'. ' 'Difference: ', result)
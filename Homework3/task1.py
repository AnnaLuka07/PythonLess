# Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

print('Введите количество цифр в списке: ')
n = int(input())

from random import randint

if n <= 0:
    print('Введите число > 0')
else:
    list = []
    
    for i in range(n):
        list.append(randint(1,10))
    print('Создадим список из', n, 'рандомных чисел: ')
    print(list)

    list1 = []
    sum = 0

    for i in range(0, len(list), 2):
        list1.append(list[i])
        sum += list[i]
    print('На нечетных позициях элементы: ', list1)
    print('Сумма этих элементов: ', sum)

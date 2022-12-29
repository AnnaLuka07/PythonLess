# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

#in
#4

#out
#[2, 5, 8, 10]
#[20, 40]

print('Введите количество цифр в списке: ')
n = int(input())

from random import randint

if n <= 0:
    print('Введите число > 0')
else:
    list = []                              
    for i in range(n):
        list.append(randint(1, 10))
    print(list)

    list1 = []
    result = 0

    for i in range(0, int(len(list) / 2), 1):
        result = list[i] * list[len(list) - i - 1]
        list1.append(result)
        i += 1
    print('Произведение пар чисел из списка ')
    print('=> ', list1)

    #i = 0                                          #тут почему-то, если вводить список из 1,3,5 - то цифры посередине без пары, тоже умножает.
    #while i < len(list) / 2:
    #    result = list[i] * list[len(list) - i - 1]
    #    list1.append(result)
    #    i += 1
    #print('=> ', list1)
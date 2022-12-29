# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

print('Введите число n ')
n = int(input())

list = []
# result = round((1 + 1/n) ** n, 3)
sum = 0

if n < 1:
    print('Введите число > 0 ')
else:
    n = range(1,n+1)
    for i in n:
        result = round((1 + 1/i) ** i, 3)
        list.append(result)
        sum += result
print(list)
print(sum)
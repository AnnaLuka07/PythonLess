#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

print("Введите число: ")
n = int(input())

p = 2             # наименьшее простое число
list = []

k = n
while p^2 <= n:
    if n % p == 0:
        list.append(p)
        n //= p
        p = 2
    else:
        p += 1
if n > 1:
    list.append(n)
print(f'Простые множители числа {k} встречаются в списке {list}')

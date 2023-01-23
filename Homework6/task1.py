#Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента. Use comprehension.

print('Введите количество цифр в списке: ')
n = int(input())

list1 = []
result_list = []

from random import randint

for i in range(n):
    list1.append(randint(1,10))
  
list = [int(i) for i in list1]
for i in range(1, len(list)):
    if list[i] > list[i-1]:
        (result_list.append(list[i]))
print("Исходный список: ", list1)
print("Список, элементы которого больше предыдущего: ", result_list)



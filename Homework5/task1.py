#Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
#in
#Number of words: 10
#out
#авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба


import random

txt = "абв"
print("Необходимо удалить из текста все слова: ", txt)
numb_word = (int(input("Введите количество слов в тексте: ")))
list1 = []
print("Рандомный текст: ")
for x in range(numb_word):
    random_txt = random.sample(txt, 3)
    list1.append("".join(random_txt))

print(" ".join(list1))

print("Текст без слов абв: ")
list2 = list(filter(lambda x: txt not in x, list1))
print(" ".join(list2))
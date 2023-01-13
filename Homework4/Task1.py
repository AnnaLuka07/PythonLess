#Вычислить число c заданной точностью d
#in
#Enter a real number: 9
#Enter the required accuracy '0.0001': 0.000001

#out
#9.000000

from decimal import Decimal

def accuracy(num, acc):
    n = Decimal(f"{num}")
    return n.quantize(Decimal(f"{acc}"))

print("Введите действительное число: ")
num = float(input())
print("Введите требуемую точность, например '0.0001': ")
acc = float(input())

print(accuracy(num,acc))









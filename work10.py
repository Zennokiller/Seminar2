# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты 
# вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть
import random
n = int(input("Введите количество монеток: "))
count_reshka = 0
count_orel = 0
for i in range(n):
    x = int(random.uniform(0, 2))
    if x==0:
        print("Решка")
    elif x==1:
        print("Орел")
    if x == 0:
        count_reshka += 1
    else:
        count_orel += 1

if count_reshka > count_orel:
    print("Нужно перевернуть ",count_orel," монетку/монеток")
else:
    print("Нужно перевернуть ",count_reshka," монетку/монеток")
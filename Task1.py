# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. 
# m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

len_n = int(input("Введите кол-во элементов множества n: "))
len_m = int(input("Введите кол-во элементов множества m: "))

n = set([int(input("Введите элемент списка n: ")) for i in range(len_n)])
m = set([int(input("Введите элемент списка m: ")) for i in range(len_m)])
intersection = list(n.intersection(m))

for i in range(len(intersection) - 1):
    if intersection[i] > intersection[i + 1]:
        temp = intersection[i + 1]
        intersection[i + 1] = intersection[i]
        intersection[i] = temp
print(intersection)
# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).


def sum_odd_index(list):
    s = 0
    for i in range(len(list)):
        if i % 2 != 1:
            s += list[i]
    print(s)


list = list(map(int, input("Введите числа через пробел: ").split()))
sum_odd_index(list)

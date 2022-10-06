# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

list_size = int(input('Enter list length: '))
default_list = []

for i in range(list_size):
    default_list.append(random.randint(0, 20))  #интервал выбран произвольно чтобы не запрашивать пользователя

print(f'Generated list is: {default_list}')

index: int = 1
sum_of_elements: int = 0

while index < len(default_list):
    sum_of_elements += default_list[index]
    index += 2

print(f'Sum of elements at not even positions of the list is: {sum_of_elements}')

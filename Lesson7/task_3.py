"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного
массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, ...

arr[m]
from statistics import median
"""
import random
m = int(input('Введит натуральное число m: '))
start_list = [random.randint(0, 100) for i in range(2 * m + 1)]

print(f'Стартовый список: {start_list}')


def func_gnome_sort(start_list):
    i, len_list = 1, len(start_list)
    while i < len_list:
        if start_list[i - 1] <= start_list[i]:
            i += 1
        else:
            start_list[i - 1], start_list[i] = start_list[i], start_list[i - 1]
            if i > 1:
                i -= 1
    return start_list



sort_list = func_gnome_sort(start_list)

print(f'Список после сортировки: {sort_list}')



def func_median(sort_list):
    quotient, remainder = divmod(len(sort_list), 2)
    if remainder:
        return sort_list[quotient]
    return sum(sort_list[quotient - 1:quotient + 1]) / 2

print(f'Медиана: {func_median(sort_list)}')
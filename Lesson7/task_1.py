"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы. Сортировка должна быть реализована в
виде функции. Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение
Обязательно сделайте замеры времени обеих реализаций
и обосновать дала ли оптимизация эффективность

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию
"""
import random
import timeit

def func_sort(start_list):

    n = 1
    while n < len(start_list):
        for i in range(len(start_list)-n):
            if start_list[i] < start_list[i+1]:
                start_list[i], start_list[i+1] = start_list[i+1], start_list[i]
        n += 1
    return start_list


start_list = [random.randint(-100, 100) for el in range(1000)]
print(f'Отсортированный список - {func_sort(start_list)}')


print(f'Время выполнения сортировки (100 раз) функцией func_sort: '
      f'{timeit.timeit("func_sort(start_list[:])", setup="from __main__ import func_sort, start_list", number=100)}')



def func_sort_upgr(start_list):
    n = 1
    m = 0
    while n < len(start_list):
        for i in range(len(start_list)-n):
            if start_list[i] < start_list[i+1]:
                start_list[i], start_list[i+1] = start_list[i+1], start_list[i]
                m = 1
        if m == 0:
            break
        n += 1
    return start_list




print(f'Отсортированный список - {func_sort_upgr(start_list)}')


print(f'Время выполнения сортировки (100 раз) функцией func_sort_upgrade: '
      f'{timeit.timeit("func_sort_upgr(start_list[:])", setup="from __main__ import func_sort_upgr, start_list", number=100)}')

# Время работы модифицированной функции (с выходом если список уже отсортирован) оптимальнее
"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Добавьте аналитику: что вы сделали и почему
"""
import timeit



def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

numbers = [el for el in range(1000)]

print(f'время выполнения функции func_1  - {timeit.timeit("func_1(numbers)", setup="from __main__ import func_1, numbers", number=1000)}')


def func_2(nums):
    new_arr = [i for i in nums[:-1] if i % 2 == 0]
    return new_arr

print(f'время выполнения оптимизированной функции func_2 - {timeit.timeit("func_2(numbers)", setup="from __main__ import func_2, numbers", number=1000)}')


# Вторая функция быстрее за счёт оптимизации времени добавления в словарь
"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
import timeit

start_list = [random.random()*50 for el in range(20)]

print(f'Первоначальный список{start_list}')


def func_sort(start_list):
    if len(start_list) > 1:
        middle = len(start_list) // 2
        left = start_list[:middle]
        right = start_list[middle:]

        func_sort(left)
        func_sort(right)

        i, j, k = 0, 0, 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                start_list[k] = left[i]
                i += 1
            else:
                start_list[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            start_list[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            start_list[k] = right[j]
            j += 1
            k += 1
        return start_list


print(f'Список после сортировки - {func_sort(start_list)}')

print(f'Время выполнения сортировки (100 раз) функцией func_sort: '
      f'{timeit.timeit("func_sort(start_list[:])", setup="from __main__ import func_sort, start_list", number=100)}')



def func_bubble_sort(start_list):
    n = 1
    while n < len(start_list):
        for i in range(len(start_list)-n):
            if start_list[i] > start_list[i+1]:
                start_list[i], start_list[i+1] = start_list[i+1], start_list[i]
        n += 1
    return start_list


print(f'Список после сортировки - {func_bubble_sort(start_list)}')

print(f'Время выполнения сортировки (100 раз) функцией func_bubble_sort: '
      f'{timeit.timeit("func_bubble_sort(start_list[:])", setup="from __main__ import func_bubble_sort, start_list", number=100)}')


#Решил сравнить время сортировки слияним и методом "пузырька", вторая сортировка по времени оптимальнее
"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните различные операции с каждым из объектов и сделайте замеры.
Опишите полученные результаты, сделайте выводы.
"""

from collections import OrderedDict
import timeit


def orderdict_func():
    orderdict = OrderedDict((str(i), i) for i in range(1000))
    for key, val in orderdict.items():
        return f'Ключ - {key}, значение - {val}'



def dict_func():
    dict = {str(i): i for i in range(1000)}
    for key, val in dict.items():
        return f'Ключ - {key}, значение - {val}'


print(f'время выполнения функции c использованием OrderedDict - {timeit.timeit("orderdict_func()", setup="from __main__ import orderdict_func", number=1000)}')
print(f'время выполнения функции без использования OrderedDict - {timeit.timeit("dict_func()", setup="from __main__ import dict_func", number=1000)}')

# использование OrderedDict заняло больше время работы функции
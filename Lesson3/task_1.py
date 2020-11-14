"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""

import time

def func_time(func):
    def function(*args):
        start_time = time.time()
        func(args[0])
        print(f'{round(time.time() - start_time,8)} миллисекунд')
    return function

@func_time
def test_list(x):
    my_list = []
    for el in range(x):
        my_list.append(el)
    return my_list

print(f'Время работы функции добавления списка:')
test_list(50000)



@func_time
def test_dict(n):
    dicts = {}
    keys = range(n)
    values = [el for el in range(n)]
    for i in keys:
        dicts[i] = values[i]
    return dicts

print(f'Время работы функции добавления словаря:')
test_dict(50000)

# Вывод: Время работы словаря медленнее
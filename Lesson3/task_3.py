"""
Задание 3.
Определить количество различных подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените хеши и множества

рара:

рар
ра
ар
ара
р
а
"""



import hashlib


def my_func(n):
    my_set = set()
    for el in range(len(n) - 1):
        for x in range(1 + el, len(n) + 1):

            my_set.add(hashlib.sha1(n[x - el - 1:x].encode()).hexdigest())
    print(my_set)
    return  my_set


my_string = input('введите строку: ')

print(f'Количество подстрок в строке "{my_string}" : {len(my_func(my_string))}')




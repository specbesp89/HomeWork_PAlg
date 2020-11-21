"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

Подсказка: примените мемоизацию

Добавьте аналитику: что вы сделали и почему
"""

import timeit

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

number = 564343
print(recursive_reverse(number))

print(f'время выполнения функции recursive_reverse  - {timeit.timeit("recursive_reverse(number)", setup="from __main__ import recursive_reverse, number", number=1000)}')




def memoize(n):
    memory = {}

    def function(*args):

        if args in memory:
            return memory[args]
        else:
            memory[args] = n(*args)
            return memory[args]
    return function

@memoize
def recursive_reverse2(number):
    if number == 0:
        return '0'
    return f'{str(number % 10)}{recursive_reverse2(number // 10)} '
print(recursive_reverse2(number))

print(f'время выполнения функции recursive_reverse2  - {timeit.timeit("recursive_reverse2(number)", setup="from __main__ import recursive_reverse2, number", number=1000)}')

#Время работы функции recursive_reverse2 быстрее за счёт реализации механизма мемоизации, т.е. за счет сохранения промежуточных решений
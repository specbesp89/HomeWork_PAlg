"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему
"""
import timeit
import cProfile




enter_num = 123456789
def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)

print(revers(enter_num))

print(f'время выполнения функции revers  - {timeit.timeit("revers(enter_num)", setup="from __main__ import revers, enter_num", number=1000)}')
cProfile.run('revers(enter_num)')

print('______________________________________________________________________________________________________________________________')


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

print(revers_2(enter_num))

print(f'время выполнения функции revers_2  - {timeit.timeit("revers_2(enter_num)", setup="from __main__ import revers_2, enter_num", number=1000)}')
cProfile.run('revers_2(enter_num)')

print('______________________________________________________________________________________________________________________________')

def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

print(revers_3(enter_num))
print(f'время выполнения функции revers_3  - {timeit.timeit("revers_3(enter_num)", setup="from __main__ import revers_3, enter_num", number=1000)}')

cProfile.run('revers_3(enter_num)')


#Вывод функция 3 наиболее эффективная потому что: 1. она единственная решена верно. 2. Время затраченное на выполнение ниже 3. отсутствуют арифметические операции
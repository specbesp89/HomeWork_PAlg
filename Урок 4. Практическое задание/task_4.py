"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
"""
import timeit


array = [1, 3, 1, 3, 4, 5, 1]

def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


print(f'время выполнения функции func_1  - {timeit.timeit("func_1()", setup="from __main__ import func_1", number=10000)}')

def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

print(f'время выполнения функции func_2  - {timeit.timeit("func_2()", setup="from __main__ import func_2", number=10000)}')



def func_3():
    number = max(array, key=array.count)
    return f"Чаще всего встречается число {number},'" \
           f" оно появилось в массиве {array.count(number)} раз(а)"



print(f'время выполнения функции func_3  - {timeit.timeit("func_3()", setup="from __main__ import func_3", number=10000)}')

def func_4():
    number = {array.count(val): val for val in set(array)}
    val = number[max(number.keys())]
    return f"Чаще всего встречается число {val},'" \
           f" оно появилось в массиве {array.count(val)} раз(а)"


print(f'время выполнения функции func_4  - {timeit.timeit("func_4()", setup="from __main__ import func_4", number=10000)}')



print(func_1())
print(func_2())
print(func_3())
print(func_4())

# время работы оптималнее у функции 3 и 1

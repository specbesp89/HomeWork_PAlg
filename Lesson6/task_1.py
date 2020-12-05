"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 1-5 ваших разных скриптов!.
Сделать их разные реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты анализа вставьте в виде комментариев к коду.
Также укажите в комментариях версию Python и разрядность вашей ОС.

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

from memory_profiler import profile



array = [1, 3, 1, 3, 4, 5, 1]


@profile
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

func_1()
"""
Зарезервировано 18.0 MiB при дальнейших операциях увеличение памяти не происходит

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    30     18.0 MiB     18.0 MiB           1   @profile
    31                                         def func_1():
    32     18.0 MiB      0.0 MiB           1       m = 0
    33     18.0 MiB      0.0 MiB           1       num = 0
    34     18.0 MiB      0.0 MiB           8       for i in array:
    35     18.0 MiB      0.0 MiB           7           count = array.count(i)
    36     18.0 MiB      0.0 MiB           7           if count > m:
    37     18.0 MiB      0.0 MiB           1               m = count
    38     18.0 MiB      0.0 MiB           1               num = i
    39     18.0 MiB      0.0 MiB           1       return f'Чаще всего встречается число {num}, ' \
    40                                                    f'оно появилось в массиве {m} раз(а)'

"""

@profile()
def dict_func():
    dict = {str(i): i for i in range(1000)}
    for key, val in dict.items():
        return f'Ключ - {key}, значение - {val}'

dict_func()

""""
Зарезервировано 18.0 MiB, на цикле происходит не существенное увеличние зарезирвированной памяти на 0.1 MiB

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    63     18.0 MiB     18.0 MiB           1   @profile()
    64                                         def dict_func():
    65     18.1 MiB      0.1 MiB        1003       dict = {str(i): i for i in range(1000)}
    66     18.1 MiB      0.0 MiB           1       for key, val in dict.items():
    67     18.1 MiB      0.0 MiB           1           return f'Ключ - {key}, значение - {val}'
"""


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width




class Asphalt_mass(Road):
    def __init__(self, _length, _width, _mass, _centimeter):
        super().__init__(_length, _width)
        self._mass = _mass
        self._centimeter = _centimeter

    def my_func(self):
        result = (self._length * self._width * self._mass * self._centimeter)/1000
        return result
@profile
def my_func():
    n = Asphalt_mass(20, 5000, 25, 5)
    print(f'Масса асфальта - {n.my_func()} тонн')

my_func()


"""
Замер функции с использованием объекта ООП показывает резервирование памяти в размере  18.1 MiB при этом дальнейшие изменения отсутсвуют
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   101     18.1 MiB     18.1 MiB           1   @profile
   102                                         def my_func():
   103     18.1 MiB      0.0 MiB           1       n = Asphalt_mass(20, 5000, 25, 5)
   104     18.1 MiB      0.0 MiB           1       print(f'Масса асфальта - {n.my_func()} тонн')

"""
@profile
def my_list_generate():
    my_list = [el for el in range(0, 100000) if el %2]
    return my_list

my_list_generate()

"""
эксперимент с генраторным выражением с генерацией большого количества елементов списка показал изначальное резервирование
памяти в размере 18.2 MiB дальнейшее увеличение памяти на 2.2 MiB
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   119     18.2 MiB     18.2 MiB           1   @profile()
   120                                         def my_list_generate():
   121     20.3 MiB      2.2 MiB      100003       my_list = [el for el in range(0, 100000) if el %2]
   122     20.3 MiB      0.0 MiB           1       return my_list

"""

@profile
def dict_func():
    dict = {str(i): i for i in range(100000)}
    for key, val in dict.items():
        return f'Ключ - {key}, значение - {val}'

dict_func()

"""
Функция герирующая словарь и возращающая ключ - значение оказалась наиболее затратная по памяти. Изначально отводится 18.0 MiB,
далее присходит прирост  памяти 15.4 MiB 
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
   138     18.0 MiB     18.0 MiB           1   @profile
   139                                         def dict_func():
   140     33.4 MiB     15.4 MiB      100003       dict = {str(i): i for i in range(100000)}
   141     33.4 MiB      0.0 MiB           1       for key, val in dict.items():
   142     33.4 MiB      0.0 MiB           1           return f'Ключ - {key}, значение - {val}'

"""

#Версия Python 3.8.6,  Windows 7 64

#Вывод первые 4 функции показали не существвенный прирост занимаемой памяти. Функция с использованием словаря
# показала наибольший прирост зарезирвированной памяти
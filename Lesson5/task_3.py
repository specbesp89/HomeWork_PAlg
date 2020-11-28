"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.
"""
import timeit
from collections import deque

simple_lst = list('Hello_world')
deq_obj = deque(simple_lst)
print(simple_lst)

#добавим элемент в конец очереди
def deque_append(list, obj):
    list.append(obj)

# добавим элемент в начало очереди
def deque_appendleft(list, obj):
    list.appendleft(obj)

#Удалим элементы
def deque_remove(list):
    list.pop()
    list.popleft()


def count_deque_func():
    n = 1000
    for i in range(n):
        deque_append(deq_obj, '!!!')
        deque_appendleft(deq_obj, ':)')
        deque_remove(deq_obj)


count_deque_func()

print(f'время выполнения функции c помощью инструмента deque - {timeit.timeit("count_deque_func()", setup="from __main__ import count_deque_func", number=1000)}')


#добавим элемент в конец очереди
def func_append(list, obj):
    list.append(obj)

# добавим элемент в начало очереди
def func_appendleft(list, obj):
    list.insert(0, obj)


#Удалим элементы
def func_remove(list):
    list.pop()
    list.pop(0)



def count_func():
    n = 1000
    for i in range(n):
        func_append(simple_lst, '!!!')
        func_appendleft(simple_lst, ':)')
        func_remove(simple_lst)

count_func()

print(f'время выполнения функции без помощи инструмента deque - {timeit.timeit("count_func()", setup="from __main__ import count_func", number=1000)}')

#Вывод инструмент deque оптимизирует время работы функции
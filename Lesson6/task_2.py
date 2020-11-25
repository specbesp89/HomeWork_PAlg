"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, библиотеки) для оптимизации памяти и
доказать! (наглядно, кодом) их эффективность (на примере профилировщика)
"""


import tracemalloc

#Начать отслеживание распределения памяти Python
tracemalloc.start()

class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)



def pal_checker(string):
    dc_obj = DequeClass()
    string = (''.join(string.split(' '))).lower()
    for el in string:
        dc_obj.add_to_rear(el)

    still_equal = True

    while dc_obj.size() > 1 and still_equal:
        first = dc_obj.remove_from_front()
        last = dc_obj.remove_from_rear()
        if first != last:
            still_equal = False

    return still_equal


print(pal_checker("молоко делили ледоколом"))


#Сделайте снимок следов блоков памяти, выделенных Python. Вернуть новый экземпляр снимка.
snapshot = tracemalloc.take_snapshot()

#Выводим статистику
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)

"""
Результат, топ 10 слотов памяти на выполнение операций: 
[ Top 10 ]
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:12: size=2484 B, count=8, average=310 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:57: size=424 B, count=1, average=424 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:46: size=416 B, count=1, average=416 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:45: size=408 B, count=1, average=408 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:36: size=136 B, count=1, average=136 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:31: size=136 B, count=1, average=136 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:28: size=136 B, count=1, average=136 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:25: size=136 B, count=1, average=136 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:22: size=136 B, count=1, average=136 B
C:/Users/Admin/PycharmProjects/HW_PythonAlgorithm/Lesson6/task_2.py:19: size=136 B, count=1, average=136 B

"""
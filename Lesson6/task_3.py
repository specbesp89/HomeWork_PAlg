"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение!
"""
from memory_profiler import profile


@profile
def recurce(value, even=0, not_even=0):
    if value == 0:
        return f'Количество четных: {even}, не четных: {not_even}'

    else:
        reduce = value % 10
        value = value//10
        if reduce % 2 == 0:
            even += 1
        else:
            not_even += 1
        return recurce(value, even, not_even)

print(recurce(34560))



"""
На мой взгляд подводным камнем в профилировании функции с рекурией быть  не однократный вызов профилирования, т.е. на каждый вызов функции. 
Таким образом, может произойти искажение в замере точного резерва памяти. В данной функции зарезервировано 18.0 MiB, дальнейшего расхода не наблюдается. 
При этом функция была вызвана 6 раз, до полного решения задания
11     18.0 MiB     18.0 MiB           6   @profile
   12                                         def recurce(value, even=0, not_even=0):
   13     18.0 MiB      0.0 MiB           6       if value == 0:
   14     18.0 MiB      0.0 MiB           1           return f'Количество четных: {even}, не четных: {not_even}'
   15                                         
   16                                             else:
   17     18.0 MiB      0.0 MiB           5           reduce = value % 10
   18     18.0 MiB      0.0 MiB           5           value = value//10
   19     18.0 MiB      0.0 MiB           5           if reduce % 2 == 0:
   20     18.0 MiB      0.0 MiB           3               even += 1
   21                                                 else:
   22     18.0 MiB      0.0 MiB           2               not_even += 1
   23     18.0 MiB      0.0 MiB           5           return recurce(value, even, not_even)

"""
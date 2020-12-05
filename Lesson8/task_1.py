"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.
КОПИПАСТ ПРИМЕРА ПРИНИМАТЬСЯ НЕ БУДЕТ!
2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.

ВНИМАНИЕ: примеры заданий будут размещены в последний день сдачи.
Но постарайтесь обойтись без них.
"""


from collections import Counter, deque



def func_haffman(string):
    # Подсчет уникальных символов
    # Counter({'t': 3, 'e': 2, ' ': 2, 'h': 1, 'r': 1, 'a': 1, 'n': 1, 'd': 1, 'o': 1, 'm': 1, 'x': 1})
    counting = Counter(string)

    # Сортируем по возрастанию количества повторений.
    # deque([('h', 1), ('r', 1), ('a', 1), ('n', 1), ('d', 1), ('o', 1), ('m', 1), ('x', 1), ('e', 2), (' ', 2), ('t', 3)])
    sort_el = deque(sorted(counting.items(), key=lambda item: item[1]))

    # Проверка, если строка состоит из одного повторяющего символа.
    if len(sort_el) != 1:
        # Цикл для построения дерева
        while len(sort_el) > 1:

            # Объединение двух крайних эл-тов
            # Определяем вес объединенного элемента
            # веса - 2, 2, 2, 2, 4, 4, 4, 7, 8, 15
            element_weight = sort_el[0][1] +  sort_el[1][1]


            #Объдиняем элмеенты с помощью combinaion
            combination = {0:  sort_el.popleft()[0], 1:  sort_el.popleft()[0]}

            '''
            {0: 'h', 1: 'r'}
            {0: 'a', 1: 'n'}
            {0: 'd', 1: 'o'}
            {0: 'm', 1: 'x'}
            {0: {0: 'm', 1: 'x'}, 1: {0: 'd', 1: 'o'}}
            {0: {0: 'a', 1: 'n'}, 1: {0: 'h', 1: 'r'}}
            {0: 'e', 1: ' '}
            {0: 't', 1: {0: 'e', 1: ' '}}
            {0: {0: {0: 'a', 1: 'n'}, 1: {0: 'h', 1: 'r'}}, 1: {0: {0: 'm', 1: 'x'}, 1: {0: 'd', 1: 'o'}}}
            {0: {0: 't', 1: {0: 'e', 1: ' '}}, 1: {0: {0: {0: 'a', 1: 'n'}, 1: {0: 'h', 1: 'r'}}, 1: {0: {0: 'm', 1: 'x'}, 1: {0: 'd', 1: 'o'}}}}

            '''

            for n, count in enumerate(sort_el):
                if element_weight > count[1]:
                    continue
                else:
                    sort_el.insert(n, (combination, element_weight))
                    break
            else:
                sort_el.append((combination, element_weight))

    else:
        # приравниваемыем значение 0 к одному повторяющемуся символу
        element_weight = sort_el[0][1]
        comb = {0:  sort_el.popleft()[0], 1: None}
        sort_el.append((comb, element_weight))

    # sort_el - deque([({0: {0: 't', 1: {0: 'e', 1: ' '}}, 1: {0: {0: {0: 'a', 1: 'n'}, 1: {0: 'h', 1: 'r'}}, 1: {0: {0: 'm', 1: 'x'}, 1: {0: 'd', 1: 'o'}}}}, 15)])

    return  sort_el[0][0]



code_dict = dict()


# haffman_tree - {0: {0: 't', 1: {0: 'e', 1: ' '}}, 1: {0: {0: {0: 'a', 1: 'n'}, 1: {0: 'h', 1: 'r'}}, 1: {0: {0: 'm', 1: 'x'}, 1: {0: 'd', 1: 'o'}}}}

def func_haffman_code(haffman_tree, path=''):

    if not isinstance(haffman_tree, dict):
        code_dict[haffman_tree] = path

    else:
        func_haffman_code(haffman_tree[0], path=f'{path}0')
        func_haffman_code(haffman_tree[1], path=f'{path}1')



def func_code(string):
    func_haffman_code(func_haffman(string))
    for el in string:
        print(code_dict[el], end=' ')


#кодируем текст "the random text"
func_code("the random text")






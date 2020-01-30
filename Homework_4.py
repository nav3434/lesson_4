# Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random)

import random

list_name = ['Andrey', 'Ivan', 'Anna', 'Natalia', 'Igor', 'Larisa', 'Petr', 'Mikle', 'Brain', 'Donald', 'Margaret',
             'Bil', 'Pavel', 'Arkadiy', 'Sergey', 'Vadim', 'Vladimir', 'Platon', 'Matvey', 'Marina']

def choice_100(name, n=100):
    return random.choices(name, k=n)

list_100 = choice_100(list_name)
print(list_100)

# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;

def often_name(name):
    sort = sorted(name)
    print(sort)
    name_oft = sort[0]      # наиболее часто употребляемое имя
    n = sort[0]             # текущее имя, для которого идет подсчет количества повторений в списке
    num_max = 1             # наибольшая частота повления имени
    i = 0                   # счетчик имен
    num = 0                 # счетчик повторений имени
    while i != len(sort):
        if sort[i] == n:
            num = num + 1
        if num_max < num:
            if i != len(sort)-1:
                if sort[i+1] != sort[i]:
                    n = sort[i + 1]
                    num_max = num
                    num = 0
            name_oft = sort[i]
        if sort[i] != sort[i-1]:
            n = sort[i]
            num = 0
        i = i + 1

    return (name_oft, num_max + 1)


print(often_name(list_100)) # получился очень запутанный алгоритм, но работает верно. Я пока не знаком с другими методами)))



# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
#
first_l = list(map(lambda x: x[0], list_100))
letter = list(set(first_l))
# n количество повторерий самой редкой буквы
# m счетчик
#l самая редкая буква

def red_l(name, lit):
    n = name.count(lit[0])
    for i in range(len(lit)):
        m = name.count(lit[i])
        if m <= n:
            n = m
            l = lit[i]
    return (l, n)

print(red_l(first_l, letter))

"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(lst):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    result = [number**2 for number in lst]
    return result

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"


def is_prime(number):
    z = 0
    i = 2
    while i <= number:
        if number % i == 0 and i <= number:
            z += 1
        i += 1
    if z <= 1:
        return number


def filter_numbers(lst, arg):
    lst_out = []
    if arg == ODD:
        while len(lst) >= 1:
            if lst[0] % 2 != 0 :
                lst_out.append(lst[0])
            lst.pop(0)
    elif arg == EVEN:
        while len(lst) >= 1:
            if lst[0] % 2 == 0:
                lst_out.append(lst[0])
            lst.pop(0)
    elif arg == PRIME:
        while len(lst) >= 1:
            if is_prime(lst[0]) == lst[0]:
                lst_out.append(lst[0])
            lst.pop(0)
    return lst_out


    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """

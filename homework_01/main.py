"""
Домашнее задание №1
Функции и структуры данных

"""

def power_numbers(*lst):
#    result = [number ** 2 for number in lst]
#    return result
    return [number ** 2 for number in lst]


    # функция, которая принимает N целых чисел,
    # и возвращает список квадратов этих чисел
    # >>> power_numbers(1, 2, 5, 7)
    # <<< [1, 4, 25, 49]



# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def prime(number):
    z = 0
    i = 2
    if number <=1:
        return False
    while i <= number:
        if number % i == 0 and i <= number:
            z += 1
        i += 1
    if z <= 1:
        return True
    else:
        return False

def odd(in_num):
    if(in_num % 2) != 0:
        return True
    else:
        return False

def even(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

def filter_numbers(lst, arg):
    lst_out = []
    if arg == ODD:
        lst_out = filter(odd,lst)
    elif arg == EVEN:
        lst_out = filter(even,lst)
    elif arg == PRIME:
        lst_out = filter(prime,lst)
    return list(lst_out)

    
    # """
    # функция, которая на вход принимает список из целых чисел,
    # и возвращает только чётные/нечётные/простые числа
    # (выбор производится передачей дополнительного аргумента)
    #
    # >>> filter_numbers([1, 2, 3], ODD)
    # <<< [1, 3]
    # >>> filter_numbers([2, 3, 4, 5], EVEN)
    # <<< [2, 4]
    # """

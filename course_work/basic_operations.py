"""Блок содержит функции выполнения стандартных математических операции:
    - "+";
    - "-";
    - "*";
    - "/".
"""

def add_numbers(number_1, number_2):
    """Возвращает сумму двух чисел"""
    return number_1 + number_2

def diff_numbers(number_1, number_2):
    """Возвращает разницу между первым и вторым числом"""
    return number_1 - number_2

def mult_numbers(number_1, number_2):
    """Возвращает произведение двух чисел"""
    return number_1 * number_2

def div_numbers(number_1, number_2):
    """Возвращает значение от деления первого числа на второе"""
    return number_1 / number_2

operators_dict = {'+': add_numbers,
                  '-': diff_numbers,
                  '*': mult_numbers,
                  '/': div_numbers
                  }
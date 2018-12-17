"""Блок содержит функции визуального преобразования чисел (более удобный вывод для чисел
"""

def check_number_format(number):
    """Возвращает значение целого числа, заданного как десятичное, в формате целого числа"""
    if number - int(number) == 0:
        return int(number)
    else:
        return number

def negative_print(number):
    """Возвращает отрицательное значение в скобках для визуализации"""
    if number < 0:
        return '(' + str(number) + ')'
    else:
        return number
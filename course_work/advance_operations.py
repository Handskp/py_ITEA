"""Блок содержит функции выполнения продвинутых математических операции:
    - "cos".
"""
import math

adv_oper_dict = {'cos': math.cos}

def degree_to_radian(number):
    """Возвращает введенное значение градусов в радианах"""
    return (number * math.pi) / 180
import math  # для вещественных значений понадобится округление вверх и вниз (не математическое)

user_number1 = float(input('введите первое число (например: 5, 10, 8.9)\n>>>'))
user_number2 = float(input('\nвведите первое число (например: 5, 10, 8.9)\n>>>'))

# определяем меньшее и большее из введенных чисел
min_user_number = min(user_number1, user_number2)
max_user_number = max(user_number1, user_number2)

# преобразовываем вещественные числа для цыкла
number_start_range = math.ceil(min_user_number)
number_end_range = math.floor(max_user_number) + 1  # +1 чтобы учесть последнее число в промежутке

suma_natural = 0

for i in range(number_start_range, number_end_range):
    suma_natural += i

# выдаем формат чисел в зависимости от введенного формата пользователем
if min_user_number - math.floor(min_user_number) == 0:
    print_user_number1 = int(min_user_number)
else:
    print_user_number1 = min_user_number

if max_user_number - math.floor(max_user_number) == 0:
    print_user_number2 = int(max_user_number)
else:
    print_user_number2 = max_user_number

print('Сумма натуральных чисел между числом {} и числом {} = {}'.format(print_user_number1, print_user_number2, suma_natural))
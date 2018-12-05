natural_number = -1

while natural_number < 0:
    user_number = int(input('Введите любое натуральное число, например: 1, 5, 987\n>>>'))

    if user_number < 0:
        print('Упс! Ввденное значение не является натуральным числом.\nНатуральные числа имеют вид: 0, 1, 2, 3 и т.д. до бесконечноти.')

    natural_number = user_number

i = 1
factorial = i

while i <= user_number:
    factorial = factorial * i
    i = i + 1

print('Факториал числа {} = {}'.format(user_number, factorial))
user_number = int(input('Введите любое натуральное число, например: 1, 5, 987\n>>>'))
i = 1
factorial = i

while i <= user_number:
    factorial = factorial * i
    i = i + 1

print('Факториал числа {} = {}'.format(user_number, factorial))
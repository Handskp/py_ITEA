user_number = int(input('Введите любое натуральное число, например: 1, 5, 987...\n>>>'))
i = 1

# первое число ряда, как начало всего, и не только - еденица. Давайте зададим его.
fibonacci_element = 1

# для расчета следующих чисел нужно определить предидущее число и предпредидущее число, давайте сделаем это и пойдем цыклом

fibonacci_prev_element = 1 # по сути оно равно первому элементу, который мы задали выше как fibonacci_element
fibonacci_prevprev_element = 0 # ну а перед еденицой всегда 0

while i < user_number:
    fibonacci_element = fibonacci_prev_element + fibonacci_prevprev_element
    fibonacci_prevprev_element = fibonacci_prev_element
    fibonacci_prev_element = fibonacci_element
    i += 1

print('А Вы знали, что в ряде Фибоначчи, под номером {}, находится число {}? Ну теперь то знаете...'.format(user_number, fibonacci_element))
import math

print('    !!!Для решения квадратного урaвнения необходимо ввести его коэфициенты a, b и с!!!    \n'\
      'Для того чтобы задать отрицательные коэфициенты, введите отрицательное число, например: -2')
a = float(input('Введите значение первого коэфициента: \n>>>'))
b = float(input('Введите значение второго коэфициента: \n>>>'))
c = float(input('Введите значение третьего коэфициента: \n>>>'))

D = b**2 - 4*a*c

if D >= 0:
    x1 = (-b + math.sqrt(D)) / 2*a
    x2 = (-b - math.sqrt(D)) / 2*a
    x_type = 'float'
else:
    x1 = complex(-b, math.sqrt(abs(D))) / 2*a
    x2 = complex(-b, -1 * math.sqrt(abs(D))) / 2*a
    x_type = 'complex_number'

if x_type == 'complex_number':
    result = 'Решением уравнения являются комплексные числа: \n x1 = ' + str(x1) + '\n x2 = ' + str(x2)
elif x1 == x2:
    result = 'Уравнение имеет один корень: \n x = ' + str(x1)
else:
    result = 'Решением уравнения являются числа: \n x1 = ' + str(x1) + '\n x2 = ' + str(x2)

print(result)
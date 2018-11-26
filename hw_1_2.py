# hw_1_2
a = float(input('Здраствуйет! \nВвведите число:\n>>>'))
b = float(input('\nВвведите еще одно число:\n>>>'))

summa = a + b
raznitsa = a - b
umnozheniye = a * b
deleniye = a / b
deleniye_na_tselo = a // b
ostacha = a % b
kvadrat_chisla = a ** b
prioritet_deystviy = (a + b) * b
modul_chisla = abs(a * -1)

# можно использовать более продвинутые функции, не знаю входит ли это в задачу, пример использования функций этой библиотеки:
import math

koren_kvadratnyi = math.sqrt(a + b)

# вывод в консоль доля пользователя
print('\nСумма ваших чисел =', summa)
print('\nРазница между первым и вторым числом =', raznitsa)
print('\nПроизведение ваших чисел =', umnozheniye)
print('\nДеление первого на второе число =', deleniye)
print('\nЦелая часть от деления первого числа на второе =', deleniye_na_tselo)
print('\nОстача от деления первого числа на второе =', ostacha)
print('\nКвадрат первого числа =', kvadrat_chisla)
print('\nА вот что выйдевыйет если додать Ваши числа, а потом умножить сумму на второе число:', prioritet_deystviy)
print('\nМодуль первого числа =', modul_chisla)
print('\nКорень из суммы ваших чисел =', summa)
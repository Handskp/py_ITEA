# добавлена функция подсчета кол-ва значений в списке для замены collections.Counter
# По коду - добавил четвертой, в остальных функциях ничего не менялось.
# Исправлена часть ввода данных, теперь как нужно - изменено в исполнении, функции не затронуло.

import string # заданная конструкция в ДЗ почемуто ругалась, не находило whitespace

def punctuation_strip(text_string):
    """Возвращает указанный текст без знаков пунктуации"""
    for i in string.punctuation:
        if i != "'":
            text_string = text_string.replace(i, "")
        else:
            continue
    return text_string

def max_len(value_list):
    """Расчитывает максимальную длинну значения в списке. (Все приводит в текст, не меняя исходные данные)"""
    values_length_all = []

    for value in value_list:
        value_length = len(value)
        values_length_all.append(value_length)

    max_len = max(values_length_all)

    return max_len

def statistics_print(dictionary, value_list):
    """Преобразовывает статистику значений к табличному виду, убирая дубликаты значений"""
    table = ''
    used_values_list = []

    for value in value_list:
        if value in dictionary and value not in used_values_list:
            table = (table + '| ' + value + (' '*(max_len(value_list) - len(value))) + ' | ' + str(dictionary[value]) + ' |\n')
            used_values_list.append(value)
        else:
            continue
    return table

def list_num_values(value_list):
    """Возвращает словарь со значениеми из списка и количеством их повторений"""
    value_list_dict = {}.fromkeys(value_list, 0)

    for value in value_list:
        value_list_dict[value] += 1

    return value_list_dict

# начало выполнения. но это не точно
print('Этот текст может быть использован как шаблон. ',
      'Пользователь может вводить текст, а может брать строки из этого шаблона.\n',
      'Чтобы закончить работу - нажмите "Enter".\n\n', sep='')

do_not_enter_text = False
text_from_user_all = ''

while do_not_enter_text == False:
    text_from_user = input('Введиет строку:\n>>>')

    if text_from_user not in string.whitespace:
        text_from_user_all = text_from_user_all + ' ' + text_from_user.replace('\n', '')
    else:
        clear_text = punctuation_strip(text_from_user_all.lower())
        word_list = clear_text.replace('\n', ' ').split()
        statistics = list_num_values(word_list)
        statistics_dict = dict(statistics)
        statistics_result = statistics_print(statistics_dict, word_list)
        print(statistics_result, '\n')
        do_not_enter_text = True
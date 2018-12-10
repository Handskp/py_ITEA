import string # заданная конструкция в ДЗ почемуто ругалась, не находило whitespace
import collections # на занятиях не разбирали, но это оптимальный вариант. Вроде.

def punctuation_strip(text_string):
    """Возвращает указанный текст без знаков пунктуации"""
    for i in string.punctuation:
        text_string = text_string.replace(i, "")
    return text_string

do_not_enter_text = False

while do_not_enter_text == False:
    text_from_user = input('"Этот текст может быть использован как шаблон. '
                           'Пользователь может вводить текст, а может брать строки из этого шаблона.\n'
                           'Чтобы закончить работу - нажмите "Enter".\n\n'
                           'Введиет строку:\n>>>')

    if text_from_user in string.whitespace:
        do_not_enter_text = True
        print('Работа завершена!')
    else:
        clear_text = punctuation_strip(text_from_user.lower())
        word_list = clear_text.split()
        word_list.sort()

        print(word_list, '\n')
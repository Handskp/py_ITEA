# исправлен ввод апострофа, не учел в этой задаче
# исправлен ввод текста, теперь собирает накопительно все что ввел пользователь

import string # заданная конструкция в ДЗ почемуто ругалась, не находило whitespace

def punctuation_strip(text_string):
    """Возвращает указанный текст без знаков пунктуации"""
    for i in string.punctuation:
        if i != "'":
            text_string = text_string.replace(i, "")
        else:
            continue
    return text_string

print('Этот текст может быть использован как шаблон. ',
      'Пользователь может вводить текст, а может брать строки из этого шаблона.\n',
      'Чтобы закончить работу - нажмите "Enter".\n\n', sep ='')

do_not_enter_text = False
text_from_user_all = ''

while do_not_enter_text == False:
    text_from_user = input('Введиет строку:\n>>>')

    if text_from_user not in string.whitespace:
        text_from_user_all = text_from_user_all + ' ' + text_from_user.replace('\n', '')
    else:
        clear_text = punctuation_strip(text_from_user_all.lower())
        word_list = clear_text.split()
        word_list.sort()

        print(word_list, '\n')
        do_not_enter_text = True
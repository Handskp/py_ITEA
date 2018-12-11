import string

def punctuation_strip(text_string):
    """Возвращает указанный текст без знаков пунктуации"""
    for i in string.punctuation:
        if i != "'":
            text_string = text_string.replace(i, "")
        else:
            continue
    return text_string

# функция по условиям ДЗ
# Фигня конечно, но глобал дополняет словарь новыми значениями если продолжить выполнение. С сохранением в файл/базу можно было бы избежать
# Результат - все слова введенны за все время работы пользователя. Хотя можна разбивать на итерации (сессии)... наверное...
user_vocabluary = {}

def get_vocabluary(text):
    """Возвращает то что нужно по условию ДЗ. Вроде."""
    global user_vocabluary

    # -----встроенная функция-----
    def text_to_list(text):
        """Возвращает список слов из текста, учитывая всякие пакости при вводе"""
        whitespace_list = list(string.whitespace) + ['  ', '   ', '    '] #больше пробелов, теоретически, быть не должно, но можно заморочится. Этот комментаррий существует специально для того, чтобы проверить возможность листать скрол
        clear_text = punctuation_strip(text)

        for i in whitespace_list:
            if i != ' ':
                clear_text.replace(i, ' ')

        text_list = clear_text.split()
        return text_list
    # -----Конец встроенной функции-----

    text_word_list = text_to_list(text)

    for value in text_word_list:
        if value not in user_vocabluary:
            key_dict = input('Слово "{}" не найдено в словаре, введите перевод: '.format(value))
            user_vocabluary.update({value: key_dict})
        else:
            continue

    return user_vocabluary

# собираем записи от пользователя и выполняем задачу
do_not_enter_text = False
text_from_user_all = ''

while do_not_enter_text == False:
    text_from_user = input('Введите текст для перевода или "end" для завершения ввода:\n>>>')

    if punctuation_strip(text_from_user).lower() == 'end':
        dict_for_user = get_vocabluary(text_from_user_all)
        print('\nА вот и Ваш словарь:\n\n', dict_for_user)

        # зацыкливаем хочет ли пользователь продолжить (try - except еще ж не учили, вроде)
        resume_work = None

        while resume_work not in ['y', 'n']:
            resume_work = input('\nХотите продолжить? (Y/N): ').lower()

        if resume_work.lower() == 'y':
            do_not_enter_text = False
        else:
            do_not_enter_text = True
            print('Работа завершена!')
    else:
        text_from_user_all = text_from_user_all + ' ' + text_from_user
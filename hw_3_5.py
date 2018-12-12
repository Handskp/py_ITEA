import string

def punctuation_strip(text_string):
    """Возвращает указанный текст без знаков пунктуации"""
    for i in string.punctuation:
        if i != "'":
            text_string = text_string.replace(i, " ")
        else:
            continue
    return text_string

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

# дополняем красотой. Но это не точно
def max_len(value_list):
    """Расчитывает максимальную длинну значения в списке. (Все приводит в текст, не меняя исходные данные)"""
    values_length_all = []

    for value in value_list:
        value_length = len(value)
        values_length_all.append(value_length)

    max_len = max(values_length_all)

    return max_len

def dict_to_table_upd(dictionary):
    """Возвращает словарь в виде таблицы, отсортированной по значению (переводу)"""
    list_keys = dictionary.keys()
    list_values = dictionary.values()

    # сортировка словаря
    def sort_key(value):
        return value[1]

    sorted_dict_items = sorted(dictionary.items(), key=sort_key)
    sorted_dict = dict(sorted_dict_items)

    table = ''
    for value in sorted_dict:
        if value in sorted_dict:
            table = (table + '| ' + value + (' ' * (max_len(list_keys) - len(value))) + ' - ' +
                     str(sorted_dict[value]) + (' ' * (max_len(list_values) - len(str(sorted_dict[value]))))  + ' |\n')
        else:
            continue

    return table

def text_translation(text):
    translation = ''

    # -----встроенная функция----- Хотя. наверное, ее надо вынести отдельно, второй раз юзаю
    def text_to_list(text):
        """Возвращает список слов из текста, учитывая всякие пакости при вводе"""
        whitespace_list = list(string.whitespace) + ['  ', '   ', '    ']  # больше пробелов, теоретически, быть не должно
        clear_text = punctuation_strip(text)

        for i in whitespace_list:
            if i != ' ':
                clear_text.replace(i, ' ')

        text_list = clear_text.split()
        return text_list
    # -----Конец встроенной функции-----

    text_word_list = text_to_list(text)
    text_vocabulary = get_vocabluary(text)

    for i in text_word_list:
        translation = translation + text_vocabulary[i]+ ' '

    return translation

#собираем записи от пользователя и выполняем задачу
do_not_enter_text = False
text_from_user_all = ''

while do_not_enter_text == False:
    text_from_user = input('Введите текст для перевода или "end" для завершения ввода:\n>>>')

    if punctuation_strip(text_from_user).lower() == 'end':
        dict_for_user = get_vocabluary(text_from_user_all)
        print('\nА вот и Ваш словарь:\n\n', dict_to_table_upd(dict_for_user),
              '\nА вот перевод текста (пунктуацию пришлось убрать, звеняйте):\n\n', text_translation(text_from_user_all), sep='')

        # зацыкливаем хочет ли пользователь продолжить (try - except еще ж не учили)
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
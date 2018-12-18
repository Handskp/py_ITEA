import string

def clear_word(word, filterstr):
    """Все ничего, но одна функция делает две разные по смыслу вещи: либо вываливает ошибку, либо заменяет символы.
    Пришлось выводить ошибочные значения не как ошибка, просто визуально. Использовать эту функцию для новой задачи,
    как миниму, не совсем коректно, исходя из требований к выводу. Но оставим как есть и настроим костылей
    """
    result = word
    i = 0
    while i < len(word):
        try:
            if word[i] in filterstr:
                new_error = word[i]
                raise ValueError(word[i], i)
            else:
                i += 1
        except ValueError as error:
            print(error)
            result = result.replace(new_error, '')
            i += 1
            continue
    return result

def punctuation_strip(text_string):
    """Возвращает указанный текст без знаков пунктуации"""
    punctuation_str = string.punctuation + string.whitespace
    for i in string.punctuation:
        if i != "'" and i != ' ':
            text_string = text_string.replace(i, " ")
        else:
            continue
    return text_string

# хоть убей, не знаю как в параметр filterstr можно добавить кирилческие знаки, кроме как задать руками
cyrylic_str = 'абвгдеёжзийклмнопрстуфхцшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦШЩЪЫЬЭЮЯ'
exception_str = cyrylic_str + string.digits

def get_eng_words(text):
    clear_text = punctuation_strip(text)
    text_after_correction = clear_word(clear_text, exception_str)
    word_list = clear_text.split()
    updated_word_list = text_after_correction.split()

    result = []
    for i in word_list:
        if i in updated_word_list:
            result.append(i.lower())

    return result

print('Ошибочные значения:')
example_text = get_eng_words('"What is world?", "World is peace!", "В Data Science язык программирования Python\tашёл широкое приминение.", "непRфвильноые сл0ва сц1фрами - 123"')
print(set(example_text))
import string

def clear_word(word, filterstr):
    """Бесполезная функция из задачи 3"""
    check_str = string.punctuation + string.whitespace + string.digits + string.ascii_letters
    result = word
    i = 0
    while i < len(word):
        if word[i] not in check_str:
            raise ValueError(word[i], i)
        elif word[i] in filterstr:
            result = result.replace(word[i], '')
            i += 1
        else:
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


def get_eng_words(text):
    clear_text = punctuation_strip(text)
    word_list = clear_text.split()
    result = []
    i = 0
    while i < len(word_list):
        try:
            word = clear_word(word_list[i], string.digits) # отсальное было подчищено на этапе формирования списка
            if word: # тут могут быть числа, их записывает как пустое значение, т к ексепшину не относятся
                result.append(word.lower())
            i += 1
        except ValueError:
            print('Слово "{}" содержит неизвестные символы'.format(word_list[i]))
            i += 1
            continue
    result = set(result)

    return result

example_text = get_eng_words('"What is world?", "World is peace!", "В Data Science язык программирования Python\tyашёл широкое приминение.", "непRфвильноые сл0ва сц1фрами - 123"')
print(set(example_text))
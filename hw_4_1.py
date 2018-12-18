def clear_word(word, filterstr):
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

# вот эту хрень надо бы разобрать поподробней
if __name__ == "__main__":
    test_str = 'S0me tесt strіng'
    exception_str = '0ес'
    print('Ошибочные значения:')
    test_res = clear_word(test_str, exception_str)
    print()
    print('Исправленный текст:')
    print(test_res)
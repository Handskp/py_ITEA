import string

def clear_word(word, filterstr):
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

# вот эту хрень надо бы разобрать поподробней
if __name__ == "__main__":
    test_str = 's0me ,/!string'
    exception_str = ',!/'
    test_res = clear_word(test_str, exception_str)
    print()
    print('Исправленный текст:')
    print(test_res)
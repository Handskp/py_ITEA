from course_work import basic_operations as b_func, calc_GUI as gui, advance_operations as adv_func

def basic_operation(number, operator):
    while True:
        try:
            user_input_number2 = gui.check_number_format(float(input('Введите второе число: ')))
            calculation_result = gui.check_number_format(
                    b_func.operators_dict[operator](number, user_input_number2))
        except ValueError:
            print('Значения задано некорректно!')
            print('Попробуйте еще раз.')
            print()
        except ZeroDivisionError:
            print('На 0 делить нельзя!')
            print('Попробуйте еще раз.')
            print()
        else:
            output_result = str(gui.negative_print(number)) + ' ' + \
                                operator + ' ' + \
                                str(gui.negative_print(user_input_number2)) + ' = ' + \
                                str(gui.negative_print(calculation_result))
            break
    return output_result

def adv_operation(number, operator):
    """Возвращает значение введенной пользователем функции"""
    calculation_result = gui.check_number_format(adv_func.adv_oper_dict[operator](adv_func.degree_to_radian(number)))
    output_result = str(operator + ' ' + \
                        str(gui.negative_print(number)) + ' = ' + \
                        str(gui.negative_print(calculation_result)))
    return output_result

# начало выполнения
list_for_output = list(b_func.operators_dict.keys()) + list(adv_func.adv_oper_dict.keys())
print('Перечень операций, которые выполняет калькулятор:')
print(list_for_output)
print('(Именно значения выше нужно использовать для корректного выполнения операций)')
print()

while True:
    try:
        user_input_number1 = gui.check_number_format(float(input('Введите число: ')))
        user_input_operator = input('Операция: ').strip()
        if user_input_operator not in b_func.operators_dict.keys() and \
            user_input_operator not in adv_func.adv_oper_dict.keys():
            raise ValueError
    except ValueError:
        print('Значения задано некорректно!')
        print('Попробуйте еще раз.')
        print()
    else:
        if user_input_operator in b_func.operators_dict.keys():
            output_result = basic_operation(user_input_number1, user_input_operator)
        else:
            output_result = adv_operation(user_input_number1, user_input_operator)
        break

print(output_result)
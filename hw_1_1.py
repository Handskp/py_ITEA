user_name = input('Здраствуйте! \nВведите, пожалуйста, ваши имя и фамилию (например - Иван Иванов)\n>>>')
print('\nДобро пожаловать, ', user_name, '!', sep='')

COURSE_START_DT = input('\nКогда вы начали обучение? (например - 19.11.2018)\n>>>')
user_birth_dt = input('\nВведите, пожалуйста, вашу дату рождения (например - 01.01.1900)\n>>>')

#парсим дату начала курса
course_day = int(COURSE_START_DT[0:2])
course_month = int(COURSE_START_DT[3:5])
course_year = int(COURSE_START_DT[6:10])

# парсим день рождения пользователя
user_birth_day = int(user_birth_dt[0:2])
user_birth_month = int(user_birth_dt[3:5])
user_birth_year = int(user_birth_dt[6:10])

# промежуточные расчеты, считаем кол-во прожитых дней по условиям задачи
age_years_temp = course_year - user_birth_year - 1
age_months_temp = course_month - user_birth_month + 11
age_days = age_years_temp*360 + age_months_temp*30 + course_day - user_birth_day + 30 # это кол-во дней до начала курса

# зная сколько дней прожил пользователь, сколь дней в месяце, сколько дней в году, можно сделать следующее...
age_years = int(age_days / 360)
age_months = int(age_days / 30)

print('\nТак на начало курса Вам было', age_days, 'дней! Ой, извините...', age_months, 'месяцев!', 'Кхм...', age_years, 'лет.', sep=' ')
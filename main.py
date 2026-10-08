from datetime import date

DIGITS = {
    '0': ['***', '* *', '* *', '* *', '***'],
    '1': ['  *', '  *', '  *', '  *', '  *'],
    '2': ['***', '  *', '***', '*  ', '***'],
    '3': ['***', '  *', '***', '  *', '***'],
    '4': ['* *', '* *', '***', '  *', '  *'],
    '5': ['***', '*  ', '***', '  *', '***'],
    '6': ['***', '*  ', '***', '* *', '***'],
    '7': ['***', '  *', '  *', '  *', '  *'],
    '8': ['***', '* *', '***', '* *', '***'],
    '9': ['***', '* *', '***', '  *', '***'],
    ' ': ['   '] * 5,
}
WEEKDAYS = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']


def read_birth_date():
    while True:
        try:
            day = int(input('Введите день рождения: '))
            month = int(input('Введите месяц рождения: '))
            year = int(input('Введите год рождения: '))
            birthday = date(year, month, day)
            if birthday > date.today():
                print('Дата рождения не может быть в будущем. Попробуйте ещё раз.\n')
                continue
            return birthday
        except ValueError:
            print('Некорректная дата. Введите целые числа и существующую дату.\n')


def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


def calculate_age(birthday, today=None):
    today = today or date.today()
    return today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))


def render_stars(birthday):
    value = birthday.strftime('%d %m %Y')
    return '\n'.join('  '.join(DIGITS[char][row] for char in value) for row in range(5))


def main():
    print('Программа для стилистического преобразования даты рождения')
    birthday = read_birth_date()
    print(f'\nДень недели: {WEEKDAYS[birthday.weekday()]}')
    print(f'Год {birthday.year} ' + ('високосный' if is_leap_year(birthday.year) else 'не високосный'))
    print(f'Возраст: {calculate_age(birthday)} лет')
    print('\nДата рождения звёздочками (ДД ММ ГГГГ):')
    print(render_stars(birthday))
    input('\nНажмите Enter, чтобы закрыть программу...')


if __name__ == '__main__':
    main()

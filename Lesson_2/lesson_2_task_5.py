month = input("Введите номер месяца: ")
month = int(month)
def month_to_season():
    if month == 12 or month == 1 or month == 2:
        return 'Зима'
    elif month >= 3 and month <= 5:
        return 'Весна'
    elif month >= 6 and month <= 8:
        return 'Лето'
    elif month >= 9 and month <= 11:
        return 'Осень'
    else:
        return 'Неправильно введён месяц'
print(month_to_season())

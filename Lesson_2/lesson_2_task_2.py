year = input("Введите год:")
year = int(year)
def is_year_leap():
    if (year % 4) == 0:
        return True
    else: 
        return False
print('Год ', year,':', is_year_leap())
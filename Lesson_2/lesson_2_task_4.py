n = input("Введите число для проверки FizzBuzz:")
n = int(n)
for FizzBuzz in range (1, n+1):
    if FizzBuzz % 3 == 0 and FizzBuzz % 5 == 0:
        print('FizzBuzz')
    elif FizzBuzz % 3 == 0:
        print('Fizz')
    elif FizzBuzz % 5 == 0:
        print('Buzz')
    else:
        print(FizzBuzz)

#Написать функцию, которая возвращает заданное число Фибоначчи. Обязательно через рекурсию.

def func(n):    
        if n in (1, 2):
            return 1
        return func(n - 1) + func(n - 2)

while True:
    try:
        n = int(input('Введите порядочный номер числа ряда Фибонначи:'))
        res = True
    except ValueError:
        print('Неверный ввод, введите число')
        res = False

    if res == True:
        print(func(n))
        break
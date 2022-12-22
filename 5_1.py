"""Функция, для проверки пароля."""

"""Подключаем нужную библиотеку, для проверки пароля в независимости от регистра"""
import string

pas = str(input('Введите пароль:'))

"""Функция для проверки пароля"""
def func(password):
    if len(password) < 6:
        return False
    """
    Устанавливаем исходные значения:
    sp[1] = False - Длина пароля 
    sp[2] = True - Пароль состоит не только из цифр
    sp[3] = True - Пароль не содержит слово password в любом регистре
    """
    sp = [False, True, True]        
    x = 0
    for letter in password:
        if letter in string.digits:
            sp[0] = True
            x += 1
        if  x == len(password):
            sp[1] = False   
        if 'password'.lower() in password.lower():
            sp[2] = False 

    """
    Сравниваем все значения и выводим результат проверки
    """        
    if all(sp):
        return True
    return False

if func(pas) == True:
    print('Пароль успешно прошел проверку')
else:
    print('Введите другой пароль в соответсвии с правилами безопасности:')
    print('Должен быть не менее 6 символов')
    print('Должен содержать хотя бы одну цифру')
    print('Не должен состоять только из цифр')
    print('Не должен содержать слово “password” в любом регистре') 
       
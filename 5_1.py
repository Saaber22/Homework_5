#Функция, для проверки пароля.
import string

pas = str(input('Введите пароль:'))

def func(password):
    if len(password) < 6:
        return False
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
       
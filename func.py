def print_menu():  
    print ('\nПожалуйста, выберите один из следующих пунктов:')  
    print('1. Добавить новый контакт')  
    print('2. Показать контакты')  
    print('3. Изменить контакты')  
    print('4. Удалить контакты')
    print('5. Найти контакты')
    print('0. Выйти из телефонной книги')


def key_pair_reception(str):
    print ("\nПожалуйста, выберите ключевое поле " + str + " (от 1 до 3)")  
    print('1. Имя')  
    print('2. Фамилия')  
    print('3. Телефонный номер')  
    print('4. Email')  
    print('5. Дата рождения')  
    print('0. Вернуться в главное меню')
    n = int(input('Ваш выбор: '))
    if n == 1:  
        field = "name"
    elif n == 2:  
        field = "surname"
    elif n == 3:  
        field = "phone_number"
    elif n == 4:  
        field = "email"
    elif n == 5:  
        field = "birth_date"
    else:
        return None
    keyword = input("\nПожалуйста введите номер операции меню: " + field + " = ")
    keypair = field + "='" + keyword + "'"
    return keypair

    


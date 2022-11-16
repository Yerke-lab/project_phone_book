import sys
import sqlite3  #загружаем библиотеку для создания базы данных 
from func import print_menu 
from func import key_pair_reception

def addcontact():
    while True:  
        name = input("Введите имя: ") 
        if len(name) != 0:  
            break  
        else:  
            print("Нужно ввести имя")     
    while True:  
        surname = input("Введите фамилию: ")  
        if len(surname) != 0:  
            break  
        else:  
            print("Нужно ввести фамилию")    
    while True:  
        num = input("Введите 10-ти значный номер телефона? (нужно вводить только цифры): ")  
        if not num.isdigit():  
            print("Пожалуйста, вводите только цифры")  
            continue  
        elif len(num) != 10:  
            print("Нужно вводить 10 цифр без пробелов и знаков")  
            continue  
        else:  
            break
    while True:  
        email = input("Введите email: ")  
        if len(email) != 0:  
            break  
    while True:  
        birth_date = input("Введите дату рождения (ГГГГ-ММ-ДД): ")  
        if len(birth_date) != 0:  
            break  
        else:  
            print("Нужно ввести дату рождения (ГГГГ-ММ-ДД)")  
    cursor.execute('''INSERT INTO phonebook (name, surname, phone_number, email, birth_date) VALUES (?,?,?,?,?)''',
                                                                         (name, surname, num, email, birth_date))  
    conn.commit()      
    print("Новый контакт " + surname + ' ' + name + " был добавлен в телефонную книгу")

def displaybook():
    cursor.execute("SELECT surname, name, phone_number, email, birth_date FROM phonebook ORDER BY surname")
    results = cursor.fetchall()
    print(results)

def editcontacts():
    s = key_pair_reception('searching')
    u = key_pair_reception('updating')
    if s != None:
        sql = "UPDATE phonebook SET " + u + " WHERE " + s
        cursor.execute(sql)
        conn.commit()
        print("Запись " + s + " удалена.\n")

def deletecontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'DELETE FROM phonebook WHERE ' + s
        cursor.execute(sql)
        conn.commit()
        print("Запись " + s + " удалена.\n")

def findcontacts():
    s = key_pair_reception('searching')
    if s != None:
        sql = 'SELECT surname, name, phone_number, email, birth_date FROM phonebook WHERE ' + s + ' ORDER BY surname'
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)


print ('\nДОБРО ПОЖАЛОВАТЬ В ТЕЛЕФОННУЮ КНИГУ')
conn = sqlite3.connect('data.db')  #Создаем базу данных и соединение с базой данных sqlite
cursor = conn.cursor()  #создаем объект cursor, который позволит делать SQL-запросы к базе
# выполнение запросов
cursor.execute('''CREATE TABLE IF NOT EXISTS phonebook (
                id integer PRIMARY KEY,
                name text NOT NULL,
                surname text,
                phone_number text,
                email text,
                birth_date text)''');
m = -1  
while m != 0:
    print_menu()  
    m = int(input('Ваш выбор: '))  
    if m == 1:  
        addcontact()
        continue
    elif m == 2:  
        displaybook()
        continue
    elif m == 3:  
        editcontacts()
        continue
    elif m == 4:  
        deletecontacts()
        continue
    elif m == 5:  
        findcontacts()
        continue
    elif m == 0:  
        print('Программа завершена.\n')
        conn.close()
        sys.exit(0)  
    else:  
        print('Пожалуйста следуйте инструкции')

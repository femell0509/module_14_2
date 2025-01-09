import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL)
''') #Создаем БД, прописываем условие, что если БД уде существует, то новую создавать не нужно
#Прописываем поля и их характеристики

# for num_user in range(1,11): # Добавили 10 пользователей со своими данными
#      cursor.execute('INSERT INTO Users(username, email, age, balance) VALUES(?,?,?,?)',(f'User{num_user}', f'example{num_user}@gmail.com', f'{num_user*10}', '1000'))

cursor.execute('UPDATE Users SET balance=? WHERE id%2=?', (500, True))

def every_number_delete(number): # Ф-я производит удаление каждого порядкового числа указонного в условии начиная с первого
    flag_delete=1
    cursor.execute('SELECT * FROM Users')
    users = cursor.fetchall()
    for i in range(len(users)+1):
        if flag_delete==1:
            cursor.execute('DELETE FROM Users WHERE id=?', (i+1,))
        flag_delete+=1
        if flag_delete==(number+1):
            flag_delete=1

every_number_delete(3) #Удалит каждую третью запись в таблице начиная с первой
cursor.execute('SELECT * FROM Users')

cursor.execute('DELETE FROM Users WHERE id=?', (6,))
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
cursor.execute('SELECT SUM(balance) FROM Users')
all_balance = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей (Вариант 1): {all_balance/total_users}')
cursor.execute('SELECT AVG(balance) FROM Users')
all_balance2 = cursor.fetchone()[0]
print(f'Средний баланс всех пользователей (Вариант 2): {all_balance2}')

connection.commit()
connection.close()
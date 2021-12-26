import sqlite3

banco = sqlite3.connect('firstDB.db')

cursor = banco.cursor()
#cursor.execute("CREATE TABLE peoople(name text, age integer )")

cursor.execute("INSERT INTO peoople VALUES ('Lucas',35)")

banco.commit()


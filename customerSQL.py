import sqlite3

conn = sqlite3.connect('customer.db')

c = conn.cursor()

#c.execute("""CREATE TABLE customers(
#        first_name text,
#       last_name text,
#       email text
#    )""")

many_custumer = [
                    ('Nathalia', 'vale', 'nath@uol.com.br'),
                    ('Osmar', 'caetano', 'os@uol.com.br'),
                    ('Eliane','do vale ','eliane,@uol.com.br'),
                ]
#c.execute("INSERT INTO customers VALUES('Lucas','Siqueira','email')")
c.executemany("INSERT INTO customers VALUES(?,?,?)", many_custumer)
conn.commit()

import  sqlite3

connection = sqlite3.connect("data.db")

cursor = connection.cursor()

create_table = "CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, username text , password text)"
cursor.execute(create_table)

create_table = "CREATE TABLE IF NOT EXISTS items(name text , price real)"
cursor.execute(create_table)
cursor.execute("INSERT INTO items VALUES('test',10.34)")
# insert_query = "INSERT INTO users VALUES (?,?,?)"
# #cursor.execute(insert_query,user)
#
# users = [(1,"jose","asdf"),
#     (2,"rolf","asdfg"),
#     (3,"anne","xyz")
# ]
# cursor.executemany(insert_query,users)
#
# select_query = "SELECT * FROM users"
# for _ in cursor.execute(select_query):
#     print(_)

connection.commit()
connection.close()

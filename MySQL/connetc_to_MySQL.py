import MySQLdb

host = "localhost"
user = "user_name"
passwd = "user_password"
db = "db_name"

connection = MySQLdb.connect(host=host, user=user,
                             passwod=passwod,
                             db=db,
                             charset="utf8")

cur = connection.cursor()

query = "SELECT * FROM table_name"

cur.execute(query)

result = cur.fetchall()

for row in result:
    print(row)

cur.close()
connection.close()
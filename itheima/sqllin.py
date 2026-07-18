from pymysql import Connection 

conn = Connection(
    host = "localhost",
    port = 3306,
    user = "root",
    password = "Lin895178",
    autocommit = True
)

print(conn.get_server_info())

cursor = conn.cursor()

conn.select_db("test")
# cursor.execute("create table test_pymysql(id int);")

cursor.execute("select * from student")

results = cursor.fetchall()

for r in results:
    print(r)

cursor.execute("insert into student values(10001, 'zhoujielun', 31, 'male')")
cursor.execute("insert into student values(10002, 'linjunjie', 32, 'male')")

# conn.commit()

conn.close()


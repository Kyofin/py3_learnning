import phoenixdb.cursor
'''
使用python3
远程连接phoneix query server服务
'''
database_url = 'http://129.28.191.99:8765/'
conn = phoenixdb.connect(database_url, autocommit=True)

cursor = conn.cursor()
cursor.execute("DROP TABLE users ")
cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username VARCHAR)")
# 如果对应PRIMARY KEY有数据就更新，没就修改
cursor.execute("UPSERT INTO users VALUES (?, ?)", (1, 'admin'))
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

cursor = conn.cursor(cursor_factory=phoenixdb.cursor.DictCursor)
cursor.execute("SELECT * FROM users WHERE id=1")
print(cursor.fetchone()['USERNAME'])

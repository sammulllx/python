import sqlite3
conn = sqlite3.connect('test.db')
cursor = conn.cursor()

# 执行查询语句:
cursor.execute('select * from user where id=?', ('1',))

# 获取查询结果集:
results = cursor.fetchall()

# 打印结果:
for row in results:
    print(row)

# 关闭Cursor:
cursor.close()
# 关闭Connection:
conn.close()

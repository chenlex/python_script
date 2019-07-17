import sqlite3
conn = sqlite3.connect('test.db')

cur = conn.cursor()
sql = "select * from New_Update"
result = cur.execute(sql)
#print(result.fetchone()) #????????????????????

for i in result.fetchone():
    print(i)
#result2 = result.fetchall()
#print(type(result2))


cur.close()
conn.close()

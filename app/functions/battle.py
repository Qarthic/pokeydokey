# Todo:
# Tie in Mon and Move classes from /app/classes and mon from /functions/generate_mon and /data, and have mon fight. Put together god awful math for types, crits, etc. 

import psycopg2

con = psycopg2.connect(
    host = "localhost",
    database = "mon_db",
    user = "postgres",
    password = "king1926",
    port = 5432
)

cur = con.cursor()

cur.execute("select * from mon where mon_element = 'Poison'")

rows = cur.fetchall()

for r in rows:
    print(r)

con.close()

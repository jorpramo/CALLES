__author__ = 'Jorge'

import pypyodbc

conn = pypyodbc.connect("DRIVER={SQL Server};SERVER=DHARMA\SQLEXPRESS;UID=loginR;PWD=loginR;DATABASE=CARRERS")

cur = conn.cursor()


def calles(municipio,provincia):
    print("SELECT top 1 * FROM VIAS where CMUM='%s' and  CPRO='%s'" % (municipio, provincia))
    cur.execute("SELECT * FROM VIAS where CMUM='%s' and  CPRO='%s'" % (municipio, provincia))
    for row in cur.fetchall():
        print(row["nviac"])


calles('250','46')

cur.close()
conn.close()
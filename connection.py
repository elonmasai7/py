import sqlite3
conn=sqlite3.connect('emobilis.db')
print("opened db succesfully")

conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (1,'Elon',18,'Mobile')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (2,'purrity',58,'mobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (3,'Joseph',18,'moi girls')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (4,'Macworld',28,'Emobilis')")
conn.execute("INSERT INTO Students(ID,NAME,AGE,SCHOOL) VALUES (5,'Lewy',898,'usiu')")

conn.commit()
print("recprds added succesfull")
conn.close()

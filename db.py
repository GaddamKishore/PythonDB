import sqlite3
conn = sqlite3.connect(":memory:")
c = conn.cursor()
table_creation_sql = "create table Capitals(State text, Capital_city text)"
c.execute(table_creation_sql)
insert_row_sql = "insert into Capitals values('Telangana','Hyderabad')"
c.execute(insert_row_sql)
insert_row_sql = "insert into Capitals values('Tamilnadu','Chennai')"
c.execute(insert_row_sql)
display_sql = "select * from Capitals"
c.execute(display_sql)

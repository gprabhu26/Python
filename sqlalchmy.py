from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String 
engine = create_engine('sqlite:///college.db', echo=True) 
meta=MetaData() 
students = Table('students', meta, Column('id', Integer, primary_key=True), 
Column('name', String), Column('lastname', String), ) 
'''meta.create_all(engine)'''
ins=students.insert()
ins=students.insert().values(name='Demo Name', lastname='Demo Last Name')
conn=engine.connect()
'''result=conn.execute(ins)
conn.execute(students.insert(), [
{'name':'Rajiv', 'lastname' : 'Khanna'},
{'name':'Komal','lastname' : 'Bhandari'},
{'name':'Abdul','lastname' : 'Sattar'},
{'name':'Priya','lastname' : 'Rajhans'},
])'''
s=students.select().where(students.c.id>=3)
conn = engine.connect()
result=conn.execute(s)
for row in result:
   print (row)

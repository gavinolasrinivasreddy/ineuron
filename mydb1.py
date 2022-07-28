import mysql.connector as conn
import pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://gsreddyphysics:reddy1985@cluster1.luyvz.mongodb.net/?retryWrites=true&w=majority")
mongo_db = client.test
print(mongo_db)

mysqlobj = conn.connect(host = "localhost" , user ="root" , passwd = "Reddy@1985", database='cnu')
print(mysqlobj)
db1 = pd.read_sql('select * from cnu.attribute',mysqlobj)
print(db1)


'''
cursor = mysqlobj.cursor()
cursor.execute('select * from attribute')
record = cursor.fetchall()
for i in record:
    print(i)
print(type(record))



cursor.execute('select distinct style from attribute;')
record1 = cursor.fetchall()
for i in record1:
    print(i)
#select count(recommendation) from attribute where recommendation = 0;
cursor.execute('select count(recommendation) from attribute where recommendation = 0;')
record2 = cursor.fetchall()
for i in record2:
    print(i)
'''
#attribute data is in the form of json
attribute_data= db1.to_json
import os 
import pymysql

# get username from cloud9 workspace
username = os.getenv("C9_USER")

# connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    # run query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # always close the connection 
    connection.close()
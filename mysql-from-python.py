import os 
import datetime
import pymysql

# get username from cloud9 workspace
username = os.getenv("C9_USER")

# connect to database
connection = pymysql.connect(host='localhost',
                            user=username,
                            password='',
                            db='Chinook')


try:
    with connection.cursor() as cursor:
        row = ("Bob", 21, "1990-06-02 23:04:56")
        cursor.execute("INSERT INTO Friends VALUES (%s, %s, %s);", row)
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # always close the connection 
    connection.close()

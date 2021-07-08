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
        list_of_names = ['Fred', 'Fred']
        format_strings = ','.join(['%s']*len(list_of_names))
        cursor.execute("DELETE FROM Friends WHERE name in ({});".format(format_strings), list_of_names)
        connection.commit()
        # Note that the above will still display a warning (not error) if the
        # table already exists
finally:
    # always close the connection
    connection.close()

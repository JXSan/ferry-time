'''
Senior Design
@Team_Members: Team Members: Jonathan, Sekani, Ishrat, Catrina
Date: March 3, 2017
'''



''' IMPORTS '''
import datetime
import mysql.connector
from mysql.connector import Error


''' IMPORTS '''

''' Connect to MySQL database - START'''
try:
    print('Connecting to MySQL database...')
    global conn
    conn = mysql.connector.connect(
        user='nyit',
        password='nyit123',
        host='45.55.186.166',
        database='ferrytime')
        
    if conn.is_connected():
        print("Connection established.")
            
        # Cursor object used to execute SQL commands.
        global cursor
        cursor = conn.cursor()

    else:
        print('Connection failed.')
        

except Error as e:
    print(e)
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import pyodbc

def connectdb():
    server = '10.200.0.252'
    database = 'db_hez'
    username = 'solist'
    password = '123456'
    cnxn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cursor = cnxn.cursor()

    # Sample select query
    cursor.execute("SELECT @@version;")
    row = cursor.fetchone()

    while row:
        print(row[0])
        row = cursor.fetchone()


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    connectdb()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

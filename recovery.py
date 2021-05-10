# Author: Ronak

import csv
from db_operations import get_recovery_connection

def create_tables(connection):
    connection.execute('''CREATE TABLE IF NOT EXISTS USER 
        (UserID	INTEGER PRIMARY KEY AUTOINCREMENT,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        Phone INTEGER NOT NULL,
        Name TEXT NOT NULL);''')

    connection.execute('''CREATE TABLE IF NOT EXISTS LOCATION 
        (LocationID INTEGER PRIMARY KEY AUTOINCREMENT,
        City TEXT NOT NULL,
        Country	TEXT NOT NULL,
        Coordinates TEXT NOT NULL);''')

    connection.execute('''CREATE TABLE IF NOT EXISTS BOOKING (
        BookingID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        StartLocation	INTEGER NOT NULL,
        EndLocation INTEGER NOT NULL,
        Type TEXT NOT NULL,
        Price REAL NOT NULL,
        StartDate TEXT NOT NULL,
        EndDate	TEXT NOT NULL,
        Status TEXT NOT NULL,
        Number INTEGER NOT NULL,
        Timestamp TEXT NOT NULL);''')

    connection.execute('''CREATE TABLE IF NOT EXISTS FEEDBACK (
        FeedbackID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        Feedback TEXT NOT NULL);''')

    connection.execute('''CREATE TABLE IF NOT EXISTS ACCOUNT (
        AccountID INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        AccountNumber INTEGER NOT NULL,
        Balance	REAL NOT NULL DEFAULT 0.00,
        CardNumber TEXT NOT NULL,
        CVV TEXT NOT NULL,
        Expiry TEXT NOT NULL,
        Password TEXT NOT NULL);''')

    connection.execute('''CREATE TABLE IF NOT EXISTS ISSUE (
        IssueID	INTEGER PRIMARY KEY AUTOINCREMENT,
        UserID INTEGER NOT NULL,
        Issue TEXT NOT NULL,
        Resolved TEXT NOT NULL DEFAULT 'NO',
        Timestamp TEXT NOT NULL);''')

    print('Tables created...')

def insert_to_db(connection, table, values):
    query = 'INSERT INTO ' + table + ' VALUES ('
    for _ in range(len(values[0])):
        query += '?,'
    query = query[:-1]
    query += ')'
    connection.executemany(query, values)
    connection.execute("COMMIT;")

def import_data(connection):
    file_names = ['ACCOUNT', 'BOOKING', 'FEEDBACK', 'ISSUE', 'LOCATION', 'USER']
    for file in file_names:
        values = []
        try:
            with open(file + '.csv') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                row_count = 0
                for row in csv_reader:
                    if(row_count == 0):
                        row_count += 1
                        continue
                    values.append(tuple(row))

                insert_to_db(connection, file, values)
        except:
            print("CSV file not found for table {}".format(file))

    print('Imported Data Successfully into REPLICATION database...')

def import_data_csv():
    connection = get_recovery_connection()
    create_tables(connection)
    import_data(connection)

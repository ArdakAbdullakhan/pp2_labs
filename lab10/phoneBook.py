import psycopg2
import csv
from configparser import ConfigParser

def read_csv(path):
    with open(path, 'r') as file:
        return [row for row in csv.DictReader(file)]

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read(filename)

    # get section, default to postgresql
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config

config = load_config()
conn = psycopg2.connect(**config)
cur = conn.cursor()

# Creating table
cur.execute("""CREATE TABLE IF NOT EXISTS PhoneBook(
    user_name VARCHAR(255),
    phone_number VARCHAR(255)
);
""")

def upload_csv_to_postgres(connection,csv_file, table_name):
    cursor = connection.cursor()
    columns = ', '.join(csv_file[0].keys())
    placeholders = ', '.join(['%s'] * len(csv_file[0]))
    insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

    # Execute the INSERT statement for each row of data
    for row in csv_file:
        cursor.execute(insert_query, list(row.values()))

    connection.commit()
    cursor.close()


def insert_phonebook_entry(user_name, phone_number):
    """ Insert a new entry into the phonebook table """
    sql = """INSERT INTO phonebook(user_name, phone_number)
             VALUES(%s, %s);"""
    
    try:
        # execute the INSERT statement
        cur.execute(sql, (user_name, phone_number))

        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update(phone_number, user_name):
    """ Update  phone number based on the user_name """
    
    updated_row_count = 0

    sql = """ UPDATE Phonebook
                SET phone_number = %s
                WHERE user_name = %s"""
    
    try:
                
        # execute the UPDATE statement
        cur.execute(sql, (phone_number, user_name))
        updated_row_count = cur.rowcount

        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return updated_row_count

def get_data():
    """ Retrieve data from the Phonebook table """
    try:
        
        cur.execute("SELECT user_name, phone_number FROM Phonebook ORDER BY user_name")
        rows = cur.fetchall()

        print("The number of phonenumbers: ", cur.rowcount)
        for row in rows:
            print(row)

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def delete_number(user_name):
    """ Delete part by user_name """

    rows_deleted  = 0
    sql = 'DELETE FROM Phonebook WHERE user_name = %s'

    try:
        # execute the UPDATE statement
        cur.execute(sql, (user_name,))
        rows_deleted = cur.rowcount

        # commit the changes to the database
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)    
    finally:
        return rows_deleted


# Read data from CSV file
datacsv = read_csv("pb.csv")

# Upload data to PostgreSQL
#upload_csv_to_postgres(datacsv, 'PhoneBook')

# Insert a new entry into the phonebook table
insert_phonebook_entry(str(input()), str(input()))

# Update user name based on phone number
update(str(input()), str(input()))


# Delete entry from the Phonebook table
deleted_rows = delete_number(str(input()))
print('The number of deleted rows: ', deleted_rows)

# Retrieve data from the Phonebook table
get_data()

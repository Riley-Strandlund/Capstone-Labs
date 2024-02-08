"""
A menu - you need to add the database and fill in the functions. 
"""
import sqlite3
# TODO create database table OR set up Peewee model to create table
db = 'juggling_records.sqlite'

def create_table():
    with sqlite3.connect(db) as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS records (name str, country str, Number_of_catches int )')
    conn.close()

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    """
    Finds all rows in the database and displays them.
    """
    conn = sqlite3.connect(db)
    cursor = conn.cursor()

    rowid = conn.execute('SELECT rowid FROM records')
    results = conn.execute('SELECT * FROM records')
    cursor.execute('SELECT COUNT(*) FROM records')
    row_count = cursor.fetchone()[0] # gets the number of rows.

    if row_count > 0:
        print("\nAll records: ")
        for row in results: # loops through the data in the database
            for thing in rowid: # gets rowid from records
                print(f'ID: {thing[0]}  Name: {row[0]:<7}  Country: {row[1]:<7}  Record: {row[2]:<7}') # :<7 = a format method where 7 represents distance.
                break # prevents reprinting data
    else:
        print("There are no records to display.")
    conn.close()
    #print('todo display all records')


def search_by_name():
    """
    Tries to find a specific name in the database to display using the whole name or a part of the name.
    """
    conn = sqlite3.connect(db)

    user_input = input('\nEnter a name to search records: ')
    query_pattern = f'%{user_input}%'
    results = conn.execute("SELECT * FROM records WHERE name LIKE ?", (query_pattern, )) # The query_pattern allows user to input the end of a name or beginning and get the record.

    if len(results.fetchall()) > 0: # if it finds a record it is printed otherwise it prints 'could not find...'
        for row in results:
            print(results)
            print(f"Name: {row[0]:<7}  Country: {row[1]:<7}  Record: {row[2]:<7}")
    else:
        print("Could not find record. Typo?")

    conn.close()
    #print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')

def add_new_record():
    """
    Allows user to create new row of data including a name, country, and catching record.
    """
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        print('Follow the below steps to create a record.')
        name = input('Input a name: ')
        country = input('Input their country: ')
        number_of_catches = int(input('Input their catch record: '))

        cursor.execute("SELECT * FROM records WHERE name = ? AND country = ? AND Number_of_catches = ?", (name, country, number_of_catches)) # compares input data to database data
        result = cursor.fetchone()

        if result is None: # if there is no record that matches the new one it is added to the database
            conn.execute("INSERT INTO records VALUES (?, ?, ?)", (name, country, number_of_catches))
        else:
            print("\nRecord already exists.")

        #print('todo add new record. What if user wants to add a record that already exists?')
    conn.close()
        


def edit_existing_record():
    """
    Allow user to change either the name, country, or catching record.
    """
    with sqlite3.connect(db) as conn:
        id_to_change = input("What is the ID of the record to change?")
        what_to_change = input("What do you want to change? Name, Country, or Record: ")

        if what_to_change.lower() == 'name':
            updated_name = input('What do you want to change the name to? ')
            conn.execute('UPDATE records SET name = ? WHERE rowid = ?', (updated_name, int(id_to_change)))
        elif what_to_change.lower() == 'country':
            updated_country = input('What do you want to change the country to? ')
            conn.execute('UPDATE records SET country = ? WHERE rowid = ?', (updated_country, int(id_to_change)))
        elif what_to_change.lower() == 'Number_of_catches':
            updated_num_of_catches = input('What do you want to change the number of catches to? ')
            conn.execute('UPDATE records SET Number_of_catches = ? WHERE rowid = ?', (updated_num_of_catches, int(id_to_change)))
        else:
            print("This is not included in records")

        #print('todo edit existing record. What if user wants to edit record that does not exist?') 
    conn.close()


def delete_record():
    """
    Deletes record corresponding to input name.
    """
    with sqlite3.connect(db) as conn:
        input_name = input('To delete a record enter a name: ')
        possible_names = []
        results = conn.execute('SELECT name FROM records') # grabs the data from the name column
        record = []
        for row in results:
            record.append(row) # unrolls the sql data   
        for item in record:
            possible_names.append(item[0]) # picks out data needed

        if input_name in possible_names:
            conn.execute('DELETE FROM records WHERE name = ?', (input_name, )) # deletes a record corresponding to the input name
            print('You have deleted a record.')
        else:
            print('That name does not exist.')    
    #print('todo delete existing record. What if user wants to delete record that does not exist?') 
    conn.close()


if __name__ == '__main__':
    create_table()
    main()
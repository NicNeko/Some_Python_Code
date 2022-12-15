import sqlite3

# prompt the user for the type of database they want to search
database_type = input('Enter "local" to search a local database or "online" to search an online database: ')

# check the user's input and choose the appropriate database connection method
if database_type.lower() == 'local':
    # specify the path to the local database file
    db_path = 'C:\\Users\\Nicolas\\Documents\\Programme Code\\Encryption\\dist\\keygen_database\\keys.db'

    # connect to the local database file
    try:
        db = sqlite3.connect(db_path)
    except sqlite3.Error as e:
        print(f'Error connecting to local database: {e}')
        exit()

elif database_type.lower() == 'online':
    # specify the connection details for the online database
    host = 'database-server'
    port = 3306
    user = 'user'
    password = 'password'
    database = 'database'

    # connect to the online database
    try:
        db = sqlite3.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database,
        )
    except sqlite3.Error as e:
        print(f'Error connecting to online database: {e}')
        exit()

else:
    print('Invalid database type')
    exit()

# create a cursor object
cursor = db.cursor()

# define a sentinel value to control the while loop
search_again = True

while search_again:
    # prompt the user for the column and value to search for
    column = input('Enter the column name to search for: ')
    value = input('Enter the value to search for: ')

    # execute the query
    try:
        cursor.execute(f"SELECT * FROM keys WHERE {column}='{value}'")
    except sqlite3.Error as e:
        print(f'Error executing query: {e}')
        db.close()
        exit()

    # get the results from the query
    results = cursor.fetchall()

    # print the results
    if results:
        # if there are any results, print a different message depending on the value of the column
        if column == 'key':
            print('Key Found')
        elif column == 'username':
            print('Username Found')
        else:
            print('Value Found')
    else:
        # if there are no results, print a message indicating that the value was not found
        print('Value not found')

    # ask the user if they want to search again
    response = input('Search again (y/n)')

    # check the user's response and set the value of the search_again variable accordingly
    if response.lower() == 'y':
        search_again = True
    elif response.lower() == 'n':
        search_again = False

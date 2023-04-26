import teradatasql
import csv
import time
import os

host = input("Zadejte adresu hostitele: ")
user = input("Zadejte jméno uživatele: ")
password = input("Zadejte heslo: ")
database = input("Zadejte název databáze: ")
table = input("Zadejte název tabulky: ")
column1 = input("Zadejte první sloupec:")
column2 = input("Zadejte druhý sloupec:")

# connection to database
con = teradatasql.connect(host={host}, user={user}, password={password}, database={database})

# SQL query to track the required table and columns
query = "SELECT {column1}, {column2} FROM {table}"

# function to save changes to csv file
def save_changes(changes, filename):
    # creates a directory if it does not exist
    if not os.path.exists('changes'):
        os.makedirs('changes')
    # creates path to the file
    filepath = os.path.join('changes', filename)
    # opens file to write the changes in
    with open(filepath, 'w', newline='') as file:
        # creates a CSV write object
        writer = csv.writer(file)
        # writes the column names as the first row
        writer.writerow(changes[0].keys())
        # writes the changes as additional lines
        for row in changes:
            writer.writerow(row.values())
    # lists where the changes were saved
    print(f"Changes saved to {filepath}")

# funcion to monitor changes
def monitor_changes(query, interval):
    # inicialization of current data
    current_data = []
    # cursor for executing sql queries
    cur = con.cursor()
    # execus sql query and adds data to current_data
    cur.execute(query)
    for row in cur:
        current_data.append(dict(zip(row.keys(), row)))
    # infinite loop to track changes
    while True:
        # waiting for the specified interval
        time.sleep(interval)
        # loading new data from the database
        new_data = []
        cur.execute(query)
        for row in cur:
            new_data.append(dict(zip(row.keys(), row)))
        # comparison of current and new data
        if current_data != new_data:
            # finds changes
            changes = [x for x in new_data if x not in current_data]
            # saves changes to file
            save_changes(changes, f"{time.time()}.csv")
            # aktualizace aktuálních dat
            current_data = new_data

# start change monitoring
monitor_changes(query, 60)
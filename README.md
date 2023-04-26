# Monitoring-script

This monitoring script connects to a Teradata database and monitors changes in a specified table and columns. It uses the teradatasql module to connect to the database, executes a SQL query to select data from the specified table and columns, and then enters an infinite loop to monitor changes in the table.

The monitor_changes() function is responsible for monitoring the changes. It executes the function at a specified interval (now set to track changes every 60 seconds) and compares the current data with the new data. If there are any changes, it saves them to a CSV file using the save_changes() function.

The save_changes() function creates a new directory called 'changes' if it does not already exist and saves the changes to a CSV file with a timestamp in the filename.

The script expects the user to input details about database and selected columns to connect to the database. Specifically, the user is requested to provide the host address, username, password, database name, table name, and two column names. These input values are then used to construct the SQL query to track the specified table and columns in the Teradata database.

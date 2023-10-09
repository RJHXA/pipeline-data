import csv
import psycopg2

csv_file = 'raw_data/nbaplayersdraft.csv'
table_name = "nbaplayers"

# with open(csv_file, 'r') as file:
#     csv_reader = csv.reader(file)


# for row in csv_reader:
#     print(row)


db_params = {
    'dbname': 'your_database_name',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'your_host',  # Usually 'localhost' if running locally
    'port': 'your_port',  # Default PostgreSQL port is 5432
}

try:
    connection = psycopg2.connect(**db_params)
except psycopg2.Error as e:
    print("Error connecting to PostgreSQL:", e)


# Generate a CREATE TABLE SQL statement
create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(header)});"

# Execute the CREATE TABLE statement
cursor.execute(create_table_sql)

# Read data from the CSV file and insert it into the SQL table
with open(csv_file, 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip the header row
    
    for row in csv_reader:
        # Generate an INSERT INTO SQL statement
        insert_sql = f"INSERT INTO {table_name} VALUES ({', '.join(['?']*len(row))});"
        
        # Execute the INSERT INTO statement
        cursor.execute(insert_sql, row)
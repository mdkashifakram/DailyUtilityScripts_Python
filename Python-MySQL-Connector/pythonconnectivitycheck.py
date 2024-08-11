import mysql.connector

# Connect to the MySQL database
config = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='PASSWORD',
    database='DATABASE'
)

# Create a c1 configect
if config.is_connected:
    c1 = config.cursor()

    # Define the query to fetch data from the CAR table
    query = "insert into car values(124,'traveller_2',18,1200000,'1 month','kolkata',24);"

    # Execute the query
    c1.execute(query)
    c1.commit()
    # # Fetch all rows from the result set
    # rows = c1.fetchall()

    # # Display the fetched data
    # for i in rows:
    #     print(i)

    # Close c1 and connection
    c1.close()
config.close()



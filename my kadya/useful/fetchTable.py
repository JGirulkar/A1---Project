

# fetch the other details of the row
def fetchColumn(cursor, file_hash):
    # fetch the other details of the row
    query_deatail = "SELECT * FROM file_data WHERE hash_values=%s"
    cursor.execute(query_deatail, (file_hash,))

# Fetch the column names of the query
    column_names = [desc[0] for desc in cursor.description]


# Fetch the result of the query
    details = cursor.fetchone()


# Print the result with column names
    print(dict(zip(column_names, details)))


def fetchWhole(cursor):

    # Execute a SELECT statement
    cursor.execute("SELECT * FROM file_data")

# Fetch the data
    data = cursor.fetchall()

# Print the data
    for row in data:
        print(row)

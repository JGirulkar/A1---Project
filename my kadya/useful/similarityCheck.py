import difflib


def percentSimilar(conn, file_hash):

    # Execute a SELECT statement to retrieve the data from the table
    with conn.cursor() as cursor:
        cursor.execute("SELECT hash_values FROM file_data")
        data = cursor.fetchall()

    # array to store hashes
    hashes = []

    # variable for max percentage match
    max_match = 0
    max_match_hash = 0

    # Loop through the data
    for row in data:
        # hashes.append(row[0])

        # Create a SequenceMatcher object with the default algorithm
        matcher1 = difflib.SequenceMatcher(None, file_hash, row[0]).ratio()
        if max_match < matcher1:
            max_match = matcher1
            max_match_hash = row[0]

    print(max_match*100)
    # print(hashes)

    # Execute a SELECT statement to retrieve the data of max match from the table
    # max_hash_query = "SELECT * FROM file_data WHERE hash_values = %s"
    # cursor.execute(max_hash_query, (max_match_hash,))

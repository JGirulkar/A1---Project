import mysql.connector
import hashlib
import difflib


# create hash
def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


file_to_check = hash_file(
    "E:\/file_detection\my kadya\media\doc-tampered.docx")


# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ja@44330022",
    database="files"
)

# Create a cursor object
cursor = conn.cursor()

# Execute a SELECT statement to retrieve the data from the table
cursor.execute("SELECT hash_values FROM file_data")

# Fetch the all data like all columns
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
    matcher1 = difflib.SequenceMatcher(None, file_to_check, row[0]).ratio()
    if max_match < matcher1:
        max_match = matcher1
        max_match_hash = row[0]

print(max_match*100)
# print(hashes)


# Execute a SELECT statement to retrieve the data of max match from the table
max_hash_query = "SELECT * FROM file_data WHERE hash_values = %s"
cursor.execute(max_hash_query, (max_match_hash,))


# Close the cursor and connection
cursor.close()
conn.close()

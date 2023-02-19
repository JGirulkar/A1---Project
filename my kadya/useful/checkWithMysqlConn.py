# this is the main file

import mysql.connector
import hashlib
import difflib
import datetime
import os
import similarityCheck
import fetchTable
import directory
import jaccardSimilarity


# establish the connection with db
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ja@44330022",
    database="files"
)


# creating cursor object
cursor = conn.cursor()


# check the connection
if conn.is_connected():
    print("connection established")
else:
    print("connection closed")


# get the list of all files and directories in the directory
files_path_list = []
directory.folder_list(files_path_list)


# generating hash of the file
# file_path = "E:\/file_detection\my kadya\media\doc.docx"
for file_path in files_path_list:
    sha3 = hashlib.sha3_256()
    with open(file_path, "rb") as f:
        while True:
            chunk = f.read(1024)
            if not chunk:
                break
            sha3.update(chunk)
    file_hash = sha3.hexdigest()
    print("The hash value of the file is: ", file_hash)
# print(type(file_hash))


# checking already present in db
    query = "SELECT COUNT(*) FROM file_data WHERE hash_values=%s"
    cursor.execute(query, (file_hash,))
    result = cursor.fetchone()
# print(type(result))
# print(result)

# if the hash is not present print the percentage match
    if result[0] == 0:
        print("Exact file not found in the database but here is the max percentage match: ")
        similarityCheck.percentSimilar(conn, file_hash)
        # jaccardSimilarity.percentSimilar(conn, file_hash)
    # insert in table
        insertQuery = "INSERT INTO file_data (hash_values, file_name, date_added) VALUES ( %s, %s, %s)"
        current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file_name = os.path.basename(file_path)
        data = (file_hash, file_name, current_time)
        cursor.execute(insertQuery, data)


# else get the details of the file found in the database
    else:
        print("File found in the database")

# fetch the other details of the row
        fetchTable.fetchColumn(cursor, file_hash)


# fetch the table
# fetchTable.fetchWhole(cursor)

# Closing cursor and connection
conn.commit()
cursor.close()
conn.close()


# check the connection closed
if conn.is_connected():
    print("connection established")
else:
    print("connection closed")

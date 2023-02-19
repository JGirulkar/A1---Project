import pymysql
import hashlib
import mysql.connector


def check_file_in_database(filename, sha1):
    # Connect to the MySQL database

    conn = pymysql.connect(host="localhost", user="root",
                           password="Ja@44330022", db="files")
    cursor = conn.cursor()

    # using mysql.connector
    # conn = mysql.connector.connect(host='localhost',
    #                                password='Ja@44330022',
    #                                user='root')

    # if conn.is_connected():
    #     print("connection established")

    # Check if the file is already present in the database
    query = "SELECT * FROM files WHERE filename=%s AND sha1=%s"
    cursor.execute(query, (filename, sha1))
    result = cursor.fetchone()
    if result:
        return True

    # File not found in the database
    return False


# Generate the SHA1 hash of the file
sha1 = hashlib.sha1()
with open("E:\/file_detection\my kadya\media\doc.docx", "rb") as f:
    chunk = 0
    while chunk != b'':
        chunk = f.read(1024)
        sha1.update(chunk)
file_sha1 = sha1.hexdigest()

# Call the function
file_found = check_file_in_database("doc", file_sha1)
if file_found:
    print("File found in the database")
else:
    print("File not found in the database")

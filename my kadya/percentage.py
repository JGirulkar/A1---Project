# this code is giving error related to unicode


import mysql.connector
import hashlib
import difflib


def hash_file(filename):
    h = hashlib.sha1()
    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
    return h.hexdigest()


cnx = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ja@44330022",
    database="files"
)

with open(
        "E:\/file_detection\my kadya\media\doc-tampered.docx", "r", encoding="UTF-8") as file_to_check:
    file_to_check.read()
file_to_check_hash = hash_file(
    "E:\/file_detection\my kadya\media\doc-tampered.docx")

query = "SELECT hash_values FROM file_data"
cursor = cnx.cursor()
cursor.execute(query)

matches = []
for (hash_value,) in cursor:
    if hash_value == file_to_check_hash:
        match = 1.0
    else:
        match = difflib.SequenceMatcher(
            None, file_to_check, hash_value).ratio()
    matches.append(match)

max_match = max(matches)
percentage_match = max_match * 100

print("Percentage match: {:.2f}%".format(percentage_match))

cursor.close()
cnx.close()

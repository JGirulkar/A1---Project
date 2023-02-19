import jaccardSimilarity
import directory
import fetchTable
import similarityCheck
from genericpath import exists
from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
import mysql.connector
from werkzeug.utils import secure_filename
import hashlib
import os
import re
from os import path
import pathlib
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile
import subprocess
from os.path import join
import os.path
import pickle
# from difflib import SequenceMatcher
# import cv2
import demo
import numpy as np
import difflib
import datetime

app = Flask(__name__)
app.secret_key = "123"

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ja@44330022",
    database="authentication"
)
mycursor = conn.cursor()
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS customer (pid INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255), contact INT, mail VARCHAR(255))")
# conn.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

    # Connect to the MySQL database
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Ja@44330022",
            database="authentication"
        )

    # Prepare a cursor object using cursor() method
        cursor = db.cursor()

    # Execute the SELECT query
        cursor.execute(
            "SELECT * FROM customer WHERE     name=%s AND mail=%s", (name,
                                                                     password)
        )

    # Fetch the results
        data = cursor.fetchone()

        if data:
            session["name"] = data[0]
            session["mail"] = data[1]
            return redirect("customer")
        else:
            flash("Username and Password     Mismatch", "danger")
        return redirect(url_for("index"))


@app.route('/customer', methods=["GET", "POST"])
def customer():
    return render_template("customer.html")


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            name = request.form['name']
            address = request.form['address']
            contact = request.form['contact']
            mail = request.form['mail']
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="Ja@44330022",
                database="authentication"
            )
            cur = conn.cursor()
            cur.execute("INSERT INTO customer (name, address, contact, mail) VALUES (%s, %s, %s, %s)",
                        (name, address, contact, mail))
            conn.commit()
            flash("Record Added  Successfully", "success")
        except:
            flash("Error in Insert Operation", "danger")
        finally:

            return redirect(url_for("index"))
            conn.close()

    return render_template('register.html')


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("index"))


@app.route('/delete/')
def delete():
    stringval = open('code/file.txt').read()
    if os.path.exists("./media/"+stringval):
        os.remove("./media/"+stringval)
    else:
        pass
    return render_template('del.html')


@app.route('/check/', methods=['POST'])
def check_files():

    # Get the uploaded folder
    uploaded_folder = request.files['folder']

   # Create a temporary directory to store the uploaded files
    # if not os.path.exists('temp'):
    #     os.makedirs('temp')
    # # Save the uploaded folder to the temporary directory
    # uploaded_folder.save(os.path.join('temp', uploaded_folder.filename))

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
            print(
                "Exact file not found in the database but here is the max percentage match: ")
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


if __name__ == '__main__':
    app.run(debug=True)

from genericpath import exists
from flask import Flask, render_template, request, flash, redirect, url_for, session, jsonify
import sqlite3
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
from difflib import SequenceMatcher
import demo


app = Flask(__name__)
app.secret_key = "123"

con = sqlite3.connect("database.db")
con.execute("create table if not exists customer(pid integer primary key,name text,address text,contact integer,mail text)")
con.close()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        con = sqlite3.connect("database.db")
        con.row_factory = sqlite3.Row
        cur = con.cursor()
        cur.execute(
            "select * from customer where name=? and mail=?", (name, password))
        data = cur.fetchone()

        if data:
            session["name"] = data["name"]
            session["mail"] = data["mail"]
            return redirect("customer")
        else:
            flash("Username and Password Mismatch", "danger")
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
            con = sqlite3.connect("database.db")
            cur = con.cursor()
            cur.execute("insert into customer(name,address,contact,mail)values(?,?,?,?)",
                        (name, address, contact, mail))
            con.commit()
            flash("Record Added  Successfully", "success")
        except:
            flash("Error in Insert Operation", "danger")
        finally:
            return redirect(url_for("index"))
            con.close()

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
    #demo.func1()
    if request.method == 'POST':
        try:
            file1 = request.files['file1']
            file2 = request.files['file2']
            global filename
            filename = secure_filename(file2.filename)
            path = os.path.abspath(filename)
            open('code/file.txt', 'w').write(filename)
            #print(filename)
            #print(path)

            msg1 = ''
            msg2 = ''
            sm = ""
            if file1:
                msg1 = 'file 1 recieved'
            else:
                msg1 = 'file 1 not recieved'
            if file2:
                msg2 = 'file 2 recieved'
            else:
                msg2 = 'file 2 not recieved'

            h1 = hashlib.sha1()
            h2 = hashlib.sha1()
            chunk = 0
            while chunk != b'':
                chunk = file1.read(1024)
                h1.update(chunk)
            chunk = 0
            while chunk != b'':
                chunk = file2.read(1024)
                h2.update(chunk)
            shamsg1 = h1.hexdigest()
            shamsg2 = h2.hexdigest()
            # print(msg1 + "\n" + msg2)
            sm = (SequenceMatcher(None, shamsg1, shamsg2).ratio()*100)

            # print(sm)

            # return jsonify (
            #     {
            # 'status': True,
            # 'message1': msg1,
            # 'message2': msg2,
            # 'sm':sm

            #     },
            # )
            if(sm < 100):
                return render_template('result.html', data={
                    'status': True,
                    'message1': msg1,
                    'message2': msg2,
                    'sm': sm
                })
            else:
                return redirect(url_for("delete"))

        except KeyError as e:
            return jsonify(
                {
                    'status': False,
                    'message': "'" + e.args[0] + "' file object not included in the form-data request"
                },
            )



if __name__ == '__main__':
    app.run(debug=True)

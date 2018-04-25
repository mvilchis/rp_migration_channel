# -*- coding: utf-8 -*-

from data.users import *
import sqlite3
from flask import g
###################### Database stuff ######################
DATABASE = '/webhook/users.db'
DATABASE ="users.db"
conn = sqlite3.connect(DATABASE,check_same_thread=False)
#Create database if not exist:
try:
    conn.execute('CREATE TABLE users (id integer primary key autoincrement, phone TEXT, id_fb TEXT, name TEXT)')
except:
    pass

def get_next_id_fb(current_id):
    next_id = list(current_id)
    found_idx = False
    #Iterate reverse
    for idx in range(len(current_id)-1,-1,-1):
        if current_id[idx] != "Z":
            next_id[idx] = chr(ord(current_id[idx]) + 1)
            found_idx = True
            break
        else:
            next_id[idx] = "A" #Reset las item
    if not found_idx: #Then add new index
        next_id +="A"
    return ''.join(next_id)

def add_user_db(phone, name ="", id_fb = None):
    if id_fb:
        this_id = id_fb
    else:
        this_phone = phone.replace(" ","")[-10:]
        phone = "+52"+this_phone
        #Get last ID:
        this_cursor = conn.execute('SELECT id_fb From users where id = (SELECT max(id) FROM users)')
        last_id = this_cursor.fetchone()[0]
        this_id = get_next_id_fb(last_id)
    with sqlite3.connect(DATABASE) as con:
        con.text_factory = str
        cursor = con.cursor()
        cursor.execute("INSERT INTO users (phone,id_fb, name) VALUES (?,?,?)",(phone,this_id,name))
    return {"id":this_id}


def get_user_by_id(id_user):
    this_cursor = conn.execute('SELECT * FROM users WHERE id_fb="%s"'%(id_user))
    contact_tuple = this_cursor.fetchone()
    if contact_tuple:
        tmp_dic= {"id":id_user,
                  "phone": contact_tuple[1][-10:],
                  "name": contact_tuple[3]}
        return tmp_dic
    return {}


def get_user_by_phone(phone):
    #Only work with last 10 digits
    this_phone = phone.replace(" ","")[-10:]
    this_cursor = conn.execute('SELECT * FROM users WHERE phone="+52%s"'%(this_phone))
    contact_tuple = this_cursor.fetchone()
    if contact_tuple:
        tmp_dic= {"id":contact_tuple[2],
                  "phone": contact_tuple[1][-10:],
                  "name": contact_tuple[3]}
        return tmp_dic
    return {}

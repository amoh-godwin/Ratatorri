import sqlite3
from time import time
conn = sqlite3.connect('test.db')
cursor = conn.cursor()


def create_table():
    return
    sql = """CREATE TABLE users (fullname text,
    email text, passcode text, country text, registered text,
    others text, win_photos text, python_gui text,
    py_gui_ufb text, pyqt text, toda text, soft_dev text,
    last_visited text)"""
    cursor.execute(sql)
    conn.commit()
    return True


def create_table_py():
    return
    sql = """CREATE TABLE python_gui (email text,
    passcode text, duration Number,
     last_visited Number)"""
    cursor.execute(sql)
    conn.commit()
    return True


def create_others_table():
    return
    sql = """CREATE TABLE others (id integer primary key,
    link text, title text, solve_modu text)"""
    cursor.execute(sql)
    conn.commit()
    return True


def alter_table():
    sql = """ALTER TABLE users ADD pratical_project_py text"""
    cursor.execute(sql)
    conn.commit()


def drop_table():
    return
    sql = """DROP TABLE python_gui"""
    cursor.execute(sql)
    conn.commit()
    return True


def delete_some():
    sql = """DELETE FROM others WHERE id='47'"""
    cursor.execute(sql)
    conn.commit()
    return True


def create_table_sh():# delete this tabel
    sql = """CREATE TABLE usheets (surry text, othrry text)"""
    cursor.execute(sql)
    conn.commit()
    return True


def create_table_name():
    return
    sql = """CREATE TABLE sru_names (name text, uses_count int)"""
    cursor.execute(sql)
    conn.commit()
    sql = """CREATE TABLE other_names (name text, uses_count int)"""
    cursor.execute(sql)
    conn.commit()
    return True


def select_names(opt):
    sql = f"""SELECT name FROM {opt}_names WHERE uses_count=0"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def update_uses(opt, opts):
    sql = f"""UPDATE {opt}_names SET uses_count=1 WHERE name={opts}"""
    cursor.execute(sql)
    conn.commit()
    return True


def add_names(pos, name_list):
    names = [(n, 0) for n in name_list]
    if pos == 'other':
        sql = """INSERT INTO other_names VALUES (?, ?)"""
    else:
         sql = """INSERT INTO sru_names VALUES (?, ?)"""

    cursor.executemany(sql, names)
    conn.commit()
    return True


def insert_user(fullname, email, passcode):
    sql = """INSERT INTO users
    (fullname, email, passcode, country, registered, others,
    win_photos, python_gui, py_gui_ufb, pyqt, toda, soft_dev, last_visited)
     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    cursor.execute(sql, (fullname, email, passcode, "False",
    "False", "False", "False", "False", "False", "False", "False",
     "False", time()))
    conn.commit()
    return True


def insert_other(link, title, expired):
    solve_modu = 'False'
    sql = """INSERT INTO others
    (link, title, solve_modu, expired)
     VALUES (?, ?, ?, ?)"""
    cursor.execute(sql, (link, title, solve_modu, expired))
    conn.commit()
    return True


def insert_dummy(db, co):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = f"""UPDATE {db} SET {co}='False'"""
    cursor.execute(sql)
    conn.commit()
    conn.close()


def add_course(co, email, passcode, duration, last_visited):
    sql = f"""INSERT INTO {co}
    (email, passcode, duration, last_visited) 
    VALUES (?, ?, ?, ?)"""
    cursor.execute(sql, (email, passcode, duration, last_visited))
    conn.commit()
    return True


def expire_other(link):
    sql = f"""UPDATE others SET expired='True' WHERE link='{link}'"""
    cursor.execute(sql)
    conn.commit()
    return True


def register_user(email):

    sql = f"""UPDATE users SET registered='True' WHERE email='{email}'"""
    print(f'sql for register user: {sql}')
    cursor.execute(sql)
    conn.commit()
    return True


def add_user_others(email, courses):
    sql = """UPDATE users SET others=? WHERE email=?"""
    # ToDo Add timestamp
    cursor.execute(sql, (courses, email))
    conn.commit()
    return True


def add_python_gui(email):
    sql = """UPDATE users SET python_gui=? WHERE email=?"""
    # ToDo Add timestamp
    cursor.execute(sql, ("True", email))
    conn.commit()
    return True


def add_users_course(email, co):
    sql = """UPDATE users SET {co}='True' WHERE email=?"""
    # ToDo Add timestamp
    cursor.execute(sql, (email))
    conn.commit()
    return True


def add_toda(email):
    sql = """UPDATE users SET toda=? WHERE email=?"""
    # ToDo Add timestamp
    cursor.execute(sql, ("True", email))
    conn.commit()
    return True


def add_soft_dev(email):
    sql = """UPDATE users SET soft_dev=? WHERE email=?"""
    # ToDo Add timestamp
    cursor.execute(sql, ("True", email))
    conn.commit()
    return True


def update_course(co, email, dura, last_v):
    sql = f"""UPDATE {co} SET duration=?, last_visited=? WHERE email=?"""
    cursor.execute(sql, (dura, last_v, email))
    conn.commit()
    return True


def select_none_others():
    sql = """SELECT email, passcode FROM users WHERE registered='True'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def select_u_others():
    sql = """SELECT email, passcode, others FROM users WHERE others!='False'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def select_none_course(course):
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = f"""SELECT email, passcode FROM users WHERE registered='True' and {course}='False'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    conn.close()
    return all


def select_all_others():
    sql = """SELECT link FROM others WHERE expired='False'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def select_index_others(i):
    # maybe delete
    sql = """SELECT id,link FROM others"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def get_other_name(link):
    sql = f"""SELECT title FROM others WHERE link='{link}'"""
    cursor.execute(sql)
    all = cursor.fetchone()
    return all


def select_y_others(email):
    sql = f"""SELECT others FROM users WHERE email='{email}'"""
    cursor.execute(sql)
    all = cursor.fetchone()
    return all


def select_course_uu(co):
    sql = f"""SELECT email, passcode FROM users WHERE {co}='True'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def select_course(co, dura):
    sql = f"""SELECT email, passcode FROM {co} WHERE duration<{dura}"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def see_unr():
    sql = """SELECT fullname, email, passcode FROM users WHERE registered='False'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def see_reg():
    sql = """SELECT email, passcode FROM users WHERE registered='True'"""
    cursor.execute(sql)
    all = cursor.fetchall()
    return all


def see_all():
    conn = sqlite3.connect('test.db')
    cursor = conn.cursor()
    sql = """SELECT * FROM users"""
    cursor.execute(sql)
    all = cursor.fetchall()
    conn.close()
    return all

import sqlite3

import datetime

SQL_SELECT = '''
    SELECT
      id, task, task_time, created
    FROM
      organizer
'''

def dict_factory(cursor,row): # делаем словарь
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
        return d

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
    return conn

#with conn:
#cur = conn.cursor()

def initialize(conn):#создает нужные нам запросы. инициализируем
    with conn:
        cursor = conn.executescript('''
        CREATE TABLE IF NOT EXISTS organizer (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        task_name TEXT NOT NULL DEFAULT '',
        task_edit TEXT NOT NULL DEFAULT '',
        task_time DATETIME,
        task_status INTEGER NOT NULL DEFAULT 0,
        created DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP)
        ''')

# таблица с названием organizer
# id для каждой задачи
# task_name  - название задачи, вводится пользователем
# task_edit - содержание задачи, вводится пользователем
# task_time  - время для выполнения задачи, вводится пользователем
# datetime - время создания задачи

def add_task_full (conn, task_name, task_edit, task_time):
    cursor =  conn.execute('''
    INSERT INTO organizer
    (task_name, task_edit, task_time) VALUES(?,?,?)
    ''', (task_name,task_edit, task_time))  #не уверена, что здесь все верно
    pk = cursor.lastrowid

def find_all(conn):
    with conn:
        cursor = conn.execute(SQL_SELECT)
        return cursor.fetchall()

def find_task_by_pk (conn, pk):
    with conn:
        cursor = conn.execute(SQL_SELECT + ' WHERE id = ?',(pk,))
        return cursor.fetchone()

def change_status(conn, task_status, pk):
        with conn:
            cursor = conn.execute('''
            UPDATE organizer SET
            task_status=?
            WHERE pk=?''', (task_status, pk))
        return pk

def change_task(conn,task_name, pk):
    with conn:
        cursor = conn.execute('''
        UPDATE organizer SET
        task_name= ?
        task_edit = ?
        task_time = ?
        WHERE pk=?''',( task_name, task_edit, task_time, pk)) #не уверена, что верно
        return pk

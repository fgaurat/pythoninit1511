#!/usr/bin/env python
import configparser
import requests
import sqlite3
import argparse


from TodoDAO import TodoDAO

def old_main():

    config = configparser.ConfigParser()
    config.read("config.ini")
    url_todos= config['DATA']['url']
    db_file = config['DB']['file']
    
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    r = requests.get(url_todos)
    todos = r.json()
    for todo in todos:
        sql ="""
        INSERT INTO todos_tbl(user_id,title,completed) 
        VALUES({userId},'{title}',{completed})
        """.format(**todo)
        cur.execute(sql)

    con.commit()    
    con.close()

    

    print(todos[0])
    print(len(todos))

def main():
    parser = argparse.ArgumentParser(description='Retrieve all todos from db in config file.')
    parser.add_argument('config',help="config file")
    # parser.add_argument('-test',help="le test")
    args = parser.parse_args()

    config = configparser.ConfigParser()
    config.read(args.config)
    db_file = config['DB']['file']    

    dao = TodoDAO(db_file=db_file)

    todos = dao.findAll()

    for todo in todos:
        print(todo.title)


if __name__ == '__main__':
    main()
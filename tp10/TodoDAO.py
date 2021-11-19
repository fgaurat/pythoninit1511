import sqlite3
from Todo import Todo

class TodoDAO:


    def __init__(self,db_file) -> None:
        self.con = sqlite3.connect(db_file)

    def findAll(self):
        cur = self.con.cursor()
        todos= []
        for row in cur.execute('SELECT id,user_id,title,completed FROM todos_tbl'):
            id = row[0]
            user_id = row[1]
            title = row[2]
            completed = row[3]

            todo = Todo(title = title,id=id, completed = completed, user_id=user_id )
            todos.append(todo)

        return todos
    

    def __del__(self):
        self.con.close()

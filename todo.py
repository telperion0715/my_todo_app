import sqlite3

class TodoDB:
    con = None
    @staticmethod
    def connectToDatabase():
        try:
            TodoDB.con = sqlite3.connect('todo.db', check_same_thread=False)
            c = TodoDB.con.cursor()
            c.execute(f'CREATE TABLE IF NOT EXISTS tasks '
                      f'(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                      f'todo_content TEXT NOT NULL, '
                      f'todo_date TEXT NOT NULL, '
                      f'todo_time TEXT, '
                      f'completed NUMERIC NOT NULL, '
                      f'reg_date TEXT NOT NULL);')
            c.execute(f'CREATE TABLE IF NOT EXISTS users '
                      f'(id INTEGER PRIMARY KEY AUTOINCREMENT, '
                      f'user_name TEXT NOT NULL, '
                      f'user_gender TEXT NOT NULL, '
                      f'user_id TEXT NOT NULL, '
                      f'user_pw TEXT NOT NULL, '
                      f'user_email TEXT NOT NULL, '
                      f'user_mobile TEXT NOT NULL, '
                      f'reg_date TEXT NOT NULL)')
            TodoDB.con.commit()
        except Exception as e:
            print(e)

    def readTodos(self):
        c = TodoDB.con.cursor()
        c.execute('SELECT * FROM tasks')
        res = c.fetchall()
        return res
    def findTodos(self, task, date):
        c = TodoDB.con.cursor()
        c.execute(f"SELECT * FROM tasks WHERE todo_content LIKE '%{task}%' AND todo_date LIKE '{date}%'")
        res = c.fetchall()
        return res

    def insertTodo(self, values):
        c = TodoDB.con.cursor()
        c.execute('INSERT INTO tasks (todo_content, todo_date, todo_time, completed, reg_date)''Values (?, ?, ?, ?, ?)', values)
        TodoDB.con.commit()
        return c.lastrowid
    def deleteTodo(self, id):
        c = TodoDB.con.cursor()
        c.execute(f'DELETE FROM tasks WHERE id={id}')
        TodoDB.con.commit()
    def updateTodo(db, values):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_content=?, todo_date=?, todo_time=?, '
                  ' completed=? WHERE id=?', values)
        TodoDB.con.commit()
    def updateTaskState(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET completed=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()
    def updateTodoContent(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_content=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()
    def updateTodoDate(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_date=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()
    def updateTodoTime(self, args):
        c = TodoDB.con.cursor()
        c.execute('UPDATE tasks SET todo_time=? WHERE id=?', (args[1], args[0]))
        TodoDB.con.commit()

    def readUsers(self):
        c = TodoDB.con.cursor()
        c.execute('SELECT * FROM users')
        res = c.fetchall()
        return res
    def findUserByName(self, name):
        c = TodoDB.con.cursor()
        c.execute(f"SELECT * FROM users WHERE user_name like '%{name}%'")
        res = c.fetchall()
        return res
    def insertUser(self, values):
        c = TodoDB.con.cursor()
        c.execute('INSERT INTO users (user_name, user_gender, '
                  'user_id, user_pw, '
                  'user_email, user_mobile, reg_date)'
                  ' VALUES (?, ?, ?, ?, ?, ?, ?)', values)
        TodoDB.con.commit()
        return c.lastrowid
    def deleteUser(self, id):
        c = TodoDB.con.cursor()
        c.execute(f'DELETE FROM users WHERE id={id}')
        TodoDB.con.commit()
    def updateUser(db, values):
        c = TodoDB.con.cursor()
        c.execute('UPDATE users SET user_name=?, user_gender=?, user_pw=?,'
                  'user_email=?, user_mobile=? WHERE id=?', values)
        TodoDB.con.commit()

import sqlite3


class StudentTable:
    def __init__(self):

        # check_same_thread=False allows sqlite3 to run in a multi threaded environment.
        # Flask is a multi threaded environment and sqlite3 will throw an error if we run it with check_same_thread=True

        self.connection = sqlite3.connect('student_manager.db', check_same_thread=False) 
        self.cursor = self.connection.cursor()
        self._initialize_database()
    
    def _initialize_database(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS student_manager (
                            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            student_name TEXT,
                            student_age INTEGER,
                            student_grade INTEGER)''')
        self.connection.commit()
    
    def close_connection(self):
        self.connection.close()
    
    def execute_query(self, query, data=None):
        
        try:
            if data:
                self.cursor.execute(query, data)
            else:
                self.cursor.execute(query)

            if query.strip().lower().startswith('select'):
                return self.cursor.fetchall()
            else:
                self.connection.commit()
                return None
        except sqlite3.IntegrityError as e:
            print(f"!!!-- SQL ERROR --!!!\nQuery: {query}\nData: {data if data else ''}\nError: {e}")

import sqlite3

DATABASE_NAME = 'users.db'

def init_db():
    """initialize the database and create the users tables"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            name TEXT PRIMARY KEY,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
def add_user(name, password):
    """Add a new user to the database"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('INSERT INTO users (name, password) VALUES (?, ?)', (name, password))
    conn.commit()
    conn.close()
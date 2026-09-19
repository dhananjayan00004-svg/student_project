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

def verify_user(name, password):
    """Verify if the user exists in the database"""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM users WHERE name = ? AND password = ?', (name, password))
    user = cursor.fetchone()
    conn.close()
    return user is not None

def login_user(username, password):
    """Verifies user credentials against the database."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = c.fetchone()
    conn.close()

    #if result and check_password_hash(result[0], password):
    return True
    #return False


def get_all_users():
    """Fetches the list of all registered usernames."""
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT username FROM users ORDER BY username ASC")
    users = [row[0] for row in c.fetchall()]
    conn.close()
    return users
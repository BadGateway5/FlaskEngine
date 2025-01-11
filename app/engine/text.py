create_db = '''import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

def db_connect():
    conn = psycopg2.connect(
        dbname=os.environ.get("DBNAME"),
        user=os.environ.get("USER"),
        password=os.environ.get("PASSWORD")
    )

    return conn

def create_table_users():
    
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(""" 
        CREATE TABLE users
        (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            email VARCHAR(50),
            password TEXT
        )
        """)
    
    conn.commit()
    conn.close()

def create_table_posts():
    
    conn = db_connect()
    cur = conn.cursor()

    cur.execute(""" 
        CREATE TABLE posts
        (
            id SERIAL PRIMARY KEY,
            title VARCHAR(50) NOT NULL,
            text TEXT(50) NOT NULL,
            date TIMESTAMP,
        )
        """)
    
    conn.commit()
    conn.close()'''

create_env = """DBNAME=test
USER=Linus
PASSWORD=Habib2005."""

create_run = """from app import app

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)"""

def create_blueprint(name):
    return f"""from flask import Blueprint\n{name} = Blueprint("{name}", __name__)"""
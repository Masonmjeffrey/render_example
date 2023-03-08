from flask import Flask
import psycopg2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://render_example_ocz5_user:IjKRb0gXpxjYwIJERcJnWVlUhtrjN3vH@dpg-cg3sfmvdvk4hn479pq70-a/render_example_ocz5")
    conn.close()
    return "Database Connection Successful"

@app.route('/db_create')
def creating():
    conn = psycopg2.connect("postgres://render_example_ocz5_user:IjKRb0gXpxjYwIJERcJnWVlUhtrjN3vH@dpg-cg3sfmvdvk4hn479pq70-a/render_example_ocz5")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS Basketball (
        First varchar(255),
        Last varchar(255),
        City varchar(255),
        Name varchar(255),
        Number int
        );
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Created"


@app.route('/db_insert')
def inserting():
    conn = psycopg2.connect("postgres://render_example_ocz5_user:IjKRb0gXpxjYwIJERcJnWVlUhtrjN3vH@dpg-cg3sfmvdvk4hn479pq70-a/render_example_ocz5")
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO Basketball (First, Last, City, Name, Number)
        Values
        ('Jayson', 'Tatum', 'Boston', 'Celtics', 0),
        ('Stephen', 'Curry', 'San Francisco', 'Warriors', 30),
        ('Nikola', 'Jokic', 'Denver', 'Nuggets', 15),
        ('Kawhi', 'Leonard', 'Los Angeles', 'Clippers', 2);
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Populated"


@app.route('/db_drop')
def dropping():
    conn = psycopg2.connect("postgres://render_example_ocz5_user:IjKRb0gXpxjYwIJERcJnWVlUhtrjN3vH@dpg-cg3sfmvdvk4hn479pq70-a/render_example_ocz5")
    cur = conn.cursor()
    cur.execute('''
        DROP TABLE Basketball;
        ''')
    conn.commit()
    conn.close()
    return "Basketball Table Successfully Dropped"
from flask import Flask
import psycopg2


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgres://render_example_ocz5_user:IjKRb0gXpxjYwIJERcJnWVlUhtrjN3vH@dpg-cg3sfmvdvk4hn479pq70-a/render_example_ocz5")
    return "Database Connection Successful"
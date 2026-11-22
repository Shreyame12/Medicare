
from flask import Flask
from db import init_db, db

app = Flask(__name__)

init_db(app)

with app.app_context():
    print("Database connected successfully!")

    print("Tables created:")

    for table in db.metadata.tables:
        print(table)
